import uvicorn
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from langchain_core.messages import HumanMessage, AIMessage
from sse_starlette.sse import EventSourceResponse
import asyncio
import json
import os
import sys
from langfuse import Langfuse
# 尝试导入 Langfuse 回调，如果本地环境没有也不报错
try:
    from langfuse.callback import CallbackHandler
except ImportError:
    CallbackHandler = None
# 移除 decorator import，避免冲突
# from langfuse.decorators import observe

# 确保能导入项目模块
sys.path.append(os.path.dirname(__file__))

from tong_agent.graph import get_graph

from fastapi import FastAPI, HTTPException, UploadFile, File
import shutil

from langchain_core.runnables.config import RunnableConfig

app = FastAPI(title="LiuAgent API", version="1.0.0")

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 确保 data 目录存在
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# ... 现有代码 ...

# 解决 Windows 下控制台输出包含 Emoji 时的 GBK 编码报错问题
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. 加载 Agent
print("🤖 正在初始化 Agent Graph...")
agent_app = get_graph() # 获取图实例 (不用 .compile()，因为 get_graph 内部已经 compile 了)

# 初始化 Langfuse 客户端 (读取环境变量)
langfuse = Langfuse()

# 2. 定义请求体模型
class ChatRequest(BaseModel):
    query: str
    thread_id: str = "default_thread" # 用于区分不同用户的会话
    user_id: str = "default_user" # 用于区分不同用户的记忆
    stream: bool = False # 是否开启流式输出

class ChatResponse(BaseModel):
    response: str
    metadata: Optional[Dict[str, Any]] = None

# 3. 核心聊天接口
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    普通聊天接口 (非流式)，等待 Agent 生成完整回答后一次性返回。
    """
    try:
        # 构造输入
        inputs = {"messages": [HumanMessage(content=request.query)]}
        
        # 1. 初始化 CallbackHandler (推荐方式)
        # 这将自动捕获整个 LangGraph 的执行作为一个 Root Trace
        callbacks = []
        if CallbackHandler is not None:
            langfuse_handler = CallbackHandler(
                session_id=request.thread_id,
                user_id=request.user_id, # 使用请求中的 user_id
                tags=["TongAgent", "Graph"]
            )
            callbacks.append(langfuse_handler)
        
        config = {
            "configurable": {
                "thread_id": request.thread_id,
                "user_id": request.user_id # 传递 user_id 到 graph 配置中
            },
            "recursion_limit": 100, # 提高递归上限，防止复杂任务提前截断
            "callbacks": callbacks, # 注入 Handler
            "run_name": "TongAgent_Main_Graph" # 设置 Root Run 的名字
        }
        
        # 调用 Agent
        final_state = await agent_app.ainvoke(inputs, config=config)
        
        # 提取最后一条 AI 回答
        last_message = final_state["messages"][-1]
        response_content = last_message.content
        
        return ChatResponse(response=response_content)

    except Exception as e:
        print(f"❌ Error processing request: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# 4. 流式聊天接口 (SSE)
@app.get("/chat/stream")
async def stream_chat_endpoint(query: str, thread_id: str = "default_thread", user_id: str = "default_user"):
    """
    流式聊天接口 (Server-Sent Events)，实时返回 Agent 的思考过程和回答。
    """
    async def event_generator():
        inputs = {"messages": [HumanMessage(content=query)]}
        
        # 1. 初始化 CallbackHandler (如果可用)
        callbacks = []
        if CallbackHandler is not None:
            langfuse_handler = CallbackHandler(
                session_id=thread_id,
                user_id=user_id, # 使用请求参数
                tags=["TongAgent", "Stream"]
            )
            callbacks.append(langfuse_handler)
        
        config = {
            "configurable": {
                "thread_id": thread_id,
                "user_id": user_id
            },
            "recursion_limit": 100, # 提高流式调用的递归上限
            "callbacks": callbacks, # 注入 Handler (如果有)
            "run_name": "TongAgent_Stream_Graph" # Root Run
        }
        
        try:
            # 使用 astream_events 获取详细的流式事件
            async for event in agent_app.astream_events(inputs, config=config, version="v1"):
                
                # 1. 监听 LLM 生成的 token (on_chat_model_stream)
                if event["event"] == "on_chat_model_stream":
                    chunk = event["data"]["chunk"]
                    if hasattr(chunk, "content") and chunk.content:
                        # 发送增量内容
                        yield {
                            "event": "message",
                            "data": json.dumps({"type": "token", "content": chunk.content})
                        }
                
                # 2. 监听工具调用开始 (on_tool_start)
                elif event["event"] == "on_tool_start":
                    tool_name = event["name"]
                    yield {
                        "event": "message",
                        "data": json.dumps({"type": "tool_start", "tool": tool_name})
                    }
                
                # 3. 监听工具调用结束 (on_tool_end)
                elif event["event"] == "on_tool_end":
                    tool_name = event["name"]
                    output = str(event["data"].get("output"))
                    yield {
                        "event": "message",
                        "data": json.dumps({"type": "tool_end", "tool": tool_name, "output": output[:200] + "..."}) # 只截取前200字
                    }
                    
                # 4. 监听节点流转（获取 Reflection 内部日志）
                elif event["event"] == "on_chain_end" and event.get("name") == "reflection_node":
                    # 从反思节点的结果中提取内容
                    try:
                        reflection_data = event["data"]["output"]
                        if reflection_data and isinstance(reflection_data, dict):
                            # 返回反思日志到前端
                            yield {
                                "event": "message",
                                "data": json.dumps({
                                    "type": "reflection_log", 
                                    "analysis": reflection_data.get("reflection", ""),
                                    "feedback": reflection_data.get("feedback_instruction", ""),
                                    "next_action": reflection_data.get("next_action", "")
                                })
                            }
                    except Exception as e:
                        pass
                
                # 5. 监听规划节点流转（获取 Planner 计划）
                elif event["event"] == "on_chain_end" and event.get("name") == "planner_node":
                    try:
                        planner_data = event["data"]["output"]
                        if planner_data and "plan" in planner_data:
                            yield {
                                "event": "message",
                                "data": json.dumps({
                                    "type": "planner_log",
                                    "plan": planner_data["plan"]
                                })
                            }
                    except Exception as e:
                        pass

        except Exception as e:
            yield {
                "event": "error",
                "data": json.dumps({"error": str(e)})
            }
            
    return EventSourceResponse(event_generator())

# 4.5 WebSocket 流式聊天接口
@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    try:
        # 接收客户端的第一条消息（配置信息或首个查询）
        data = await websocket.receive_text()
        request_data = json.loads(data)
        
        query = request_data.get("query", "")
        thread_id = request_data.get("thread_id", "default_thread")
        user_id = request_data.get("user_id", "default_user")
        
        inputs = {"messages": [HumanMessage(content=query)]}
        
        # 1. 初始化 CallbackHandler (如果可用)
        callbacks = []
        if CallbackHandler is not None:
            langfuse_handler = CallbackHandler(
                session_id=thread_id,
                user_id=user_id,
                tags=["TongAgent", "WebSocket"]
            )
            callbacks.append(langfuse_handler)
            
        # 恢复成普通的字典，LangGraph 的底层能最好地解析字典格式的配置
        config = {
            "configurable": {
                "thread_id": thread_id,
                "user_id": user_id
            },
            "recursion_limit": 250, # 进一步提高流式调用的递归上限，防止复杂多步任务截断
            "callbacks": callbacks,
            "run_name": "TongAgent_WS_Graph"
        }
        
        try:
            # 直接把 config 字典传给 astream_events，不要用 with_config，这和后台测试脚本完全一致
            async for event in agent_app.astream_events(inputs, config=config, version="v1"):
                
                # 1. 监听 LLM 生成的 token (on_chat_model_stream)
                if event["event"] == "on_chat_model_stream":
                    # 获取当前所属的节点名（如果有的话）
                    tags = event.get("tags", [])
                    metadata = event.get("metadata", {})
                    current_node = metadata.get("langgraph_node", "")
                    
                    # 为了防止过滤过严导致前端无输出，我们采用“排除法”：
                    # 默认允许输出所有模型生成的文字，除非它明确属于中间推理节点
                    is_generating_response = True
                    
                    # 明确的中间推理节点，其流式文字不应直接展示给用户
                    if "planner" in tags or "reflection" in tags or "continue_logic" in tags:
                        is_generating_response = False
                    if current_node in ["planner_node", "reflection_node", "continue_logic_node", "classifier_node", "summarize_conversation_node", "intent_parse_node"]:
                        is_generating_response = False
                        
                    chunk = event["data"]["chunk"]
                    
                    # 过滤掉带有工具调用的块（因为那是给系统的指令，不是给人看的）
                    if hasattr(chunk, "tool_call_chunks") and chunk.tool_call_chunks:
                        is_generating_response = False
                    if hasattr(chunk, "tool_calls") and chunk.tool_calls:
                        is_generating_response = False
                        
                    if hasattr(chunk, "content") and chunk.content and is_generating_response:
                        # print(f"DEBUG STREAM: sending token, current_node={current_node}, tags={tags}")
                        await websocket.send_text(json.dumps({
                            "type": "token", 
                            "content": chunk.content
                        }))
                        
                # 2. 监听工具调用开始 (on_tool_start)
                elif event["event"] == "on_tool_start":
                    tool_name = event["name"]
                    await websocket.send_text(json.dumps({
                        "type": "tool_start", 
                        "tool": tool_name
                    }))
                    
                # 3. 监听工具调用结束 (on_tool_end)
                elif event["event"] == "on_tool_end":
                    tool_name = event["name"]
                    output = str(event["data"].get("output"))
                    await websocket.send_text(json.dumps({
                        "type": "tool_end", 
                        "tool": tool_name, 
                        "output": output[:200] + "..."
                    }))
                    
                # 4. 监听节点流转（获取 Reflection 内部日志）
                elif event["event"] == "on_chain_end" and event.get("name") == "reflection_node":
                    try:
                        reflection_data = event["data"]["output"]
                        if reflection_data and isinstance(reflection_data, dict):
                            await websocket.send_text(json.dumps({
                                "type": "reflection_log", 
                                "analysis": reflection_data.get("reflection", ""),
                                "feedback": reflection_data.get("feedback_instruction", ""),
                                "next_action": reflection_data.get("next_action", "")
                            }))
                    except Exception as e:
                        pass
                        
                # 5. 监听规划节点流转（获取 Planner 计划）
                elif event["event"] == "on_chain_end" and event.get("name") == "planner_node":
                    try:
                        planner_data = event["data"]["output"]
                        if planner_data and "plan" in planner_data:
                            await websocket.send_text(json.dumps({
                                "type": "planner_log",
                                "plan": planner_data["plan"]
                            }))
                    except Exception as e:
                        pass
                        
                # 6. 监听知识提炼节点流转（获取 Knowledge Extracted）
                elif event["event"] == "on_chain_end" and event.get("name") == "continue_logic_node":
                    try:
                        continue_data = event["data"]["output"]
                        if continue_data and "knowledge_record" in continue_data:
                            # 如果包含 extracted_knowledge 并且不为空，就推送到前端
                            extracted_knowledge = continue_data.get("knowledge_record", "")
                            if extracted_knowledge:
                                await websocket.send_text(json.dumps({
                                    "type": "knowledge_extracted",
                                    "content": extracted_knowledge
                                }))
                    except Exception as e:
                        pass
                
                # 7. 终极兜底：确保最终回复一定能送达前端
                elif event["event"] == "on_chain_end" and event.get("name") in ["generate_response_node", "generate_response"]:
                    print(f"DEBUG WS: Caught on_chain_end for {event.get('name')}")
                    try:
                        final_data = event["data"]["output"]
                        if final_data and "messages" in final_data and len(final_data["messages"]) > 0:
                            final_msg = final_data["messages"][-1].content
                            print(f"DEBUG WS: Sending final message fallback, length: {len(final_msg)}")
                            if final_msg:
                                # 以特殊格式发送，或者直接作为一大段 token 发送，以防前面的流式没捕获到
                                await websocket.send_text(json.dumps({
                                    "type": "token",
                                    "content": "\n\n" + final_msg
                                }))
                    except Exception as e:
                        print(f"DEBUG WS: Exception in fallback: {e}")
                        pass
                        
            # 发送结束信号
            await websocket.send_text(json.dumps({"type": "end"}))
            
        except Exception as e:
            await websocket.send_text(json.dumps({"type": "error", "error": str(e)}))
            
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"WebSocket Error: {e}")
        try:
            await websocket.close(code=1011, reason=str(e))
        except:
            pass

# 5. 健康检查
@app.get("/health")
def health_check():
    return {"status": "ok", "service": "LiuAgent"}

# 6. 文件上传接口
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    接收用户从前端上传的文件，并保存到本地 data 目录。
    同时，如果全局 E2B 沙箱处于激活状态，将其同步到沙箱中。
    """
    try:
        file_location = os.path.join(DATA_DIR, file.filename)
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
            
        # 尝试推送到 E2B 沙箱 (非阻塞)
        try:
            from tong_agent.tools.code_interpreter_tool import _global_sandbox
            if _global_sandbox is not None and _global_sandbox.is_running:
                remote_path = f"/home/user/{file.filename}"
                with open(file_location, "rb") as f:
                    _global_sandbox.files.write(remote_path, f.read())
                print(f"✅ 文件 {file.filename} 已成功推送到 E2B 沙箱的 {remote_path}")
        except Exception as e:
            print(f"⚠️ 文件上传成功，但推送到 E2B 沙箱失败: {e}")

        return {"info": f"文件 '{file.filename}' 上传成功，路径: {file_location}", "filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"文件上传失败: {e}")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=False)
