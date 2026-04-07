import streamlit as st
import requests
import json
import uuid
import os

# 获取后端地址 (优先读取环境变量，默认回退到 localhost)
# 注意：在 Docker Host 模式下，localhost 可能不通，建议在 docker-compose 中配置 API_BASE_URL
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# 设置页面配置
st.set_page_config(
    page_title="LiuAgent - 智能中间件助手",
    page_icon="🤖",
    layout="wide"
)

# 初始化 Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
    # 添加欢迎语
    st.session_state.messages.append({
        "role": "assistant",
        "content": "你好！我是 LiuAgent，一个全能的通用智能助手。\n你可以问我任何问题，无论是日常闲聊、知识查询，还是复杂的任务规划与执行。"
    })

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "user_id" not in st.session_state:
    st.session_state.user_id = "user_" + str(uuid.uuid4())[:8] # 默认生成一个随机用户ID

# 侧边栏
with st.sidebar:
    st.title("🤖 LiuAgent")
    st.markdown("---")
    
    # 用户 ID 设置
    user_id_input = st.text_input("User ID (用于记忆隔离)", value=st.session_state.user_id)
    if user_id_input != st.session_state.user_id:
        st.session_state.user_id = user_id_input
        st.success(f"User ID 已更新为: {st.session_state.user_id}")
    
    st.markdown("---")
    st.markdown("### 📁 文件上传")
    uploaded_file = st.file_uploader("上传文件给 Agent 分析", type=["log", "txt", "csv", "json"])
    if uploaded_file is not None:
        if st.button("确认上传并推送到沙箱"):
            with st.spinner("正在上传文件..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
                    res = requests.post(f"{API_BASE_URL}/upload", files=files)
                    if res.status_code == 200:
                        st.success(f"✅ 文件 {uploaded_file.name} 上传成功！")
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": f"系统提示：我已经接收到了你上传的文件 `{uploaded_file.name}`，并已将其放入我的工作目录。你可以随时让我读取和分析它了。"
                        })
                    else:
                        st.error(f"❌ 上传失败: {res.text}")
                except Exception as e:
                    st.error(f"❌ 连接错误: {e}")
                    
    st.markdown("---")
    st.markdown("### 🛠️ 功能")
    if st.button("清除对话历史"):
        st.session_state.messages = []
        st.session_state.thread_id = str(uuid.uuid4())
        st.rerun()
    
    st.markdown("---")
    st.caption(f"Thread ID: {st.session_state.thread_id}")

# 主聊天界面
st.title("💬 LiuAgent 对话")

# 1. 渲染历史消息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 2. 处理用户输入
if prompt := st.chat_input("请输入你的问题..."):
    # 显示用户消息
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 显示 AI 正在思考
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # 3. 调用后端流式接口 (WebSocket)
        try:
            import websockets
            import asyncio
            
            async def connect_and_stream():
                ws_url = "ws://localhost:8000/ws/chat"
                
                # 初始化一个用于显示思考过程的 status 面板，默认展开，并在标题上显示状态
                think_status = st.status("🤖 Agent 正在思考和执行任务...", expanded=True)
                think_placeholder = think_status.empty()
                thought_content = ""
                
                # 我们在类中共享这个变量，或者通过返回值传递
                local_full_response = ""
                
                try:
                    async with websockets.connect(ws_url) as websocket:
                        # 发送第一条消息
                        await websocket.send(json.dumps({
                            "query": prompt,
                            "thread_id": st.session_state.thread_id,
                            "user_id": st.session_state.user_id
                        }))
                        
                        while True:
                            try:
                                response = await websocket.recv()
                                data = json.loads(response)
                                
                                # 处理 token (逐字输出回答)
                                if data.get("type") == "token":
                                    content = data.get("content", "")
                                    local_full_response += content
                                    
                                    # --- 解析并分离思考过程 ---
                                    import re
                                    display_text = local_full_response
                                    llm_thoughts = ""
                                    
                                    # 1. 提取并移除 <think>...</think> 或未闭合的 <think> 标签 (DeepSeek 等模型)
                                    think_pattern = re.compile(r'<think>(.*?)(?:</think>|$)', re.DOTALL)
                                    thinks = think_pattern.findall(display_text)
                                    if thinks:
                                        for t in thinks:
                                            if t.strip():
                                                llm_thoughts += f"{t.strip()}\n\n"
                                    display_text = think_pattern.sub('', display_text)
                                    
                                    # 2. 提取并移除 "Thought: " 行 (ReAct 风格模型)
                                    lines = display_text.split('\n')
                                    clean_lines = []
                                    # 增加对 COMPLEX 这种大段 JSON 思考日志的过滤
                                    is_in_complex_log = False
                                    for line in lines:
                                        if line.strip().startswith('Thought:') or line.strip().startswith('Action:') or line.strip().startswith('Observation:'):
                                            llm_thoughts += f"🤔 {line.strip()}\n\n"
                                        elif line.strip().startswith('COMPLEX[') or line.strip().startswith('{ "sub_queries"'):
                                            # 这是后端工具调用产生的乱码，将其归入思考日志并过滤掉
                                            llm_thoughts += f"⚙️ {line.strip()}\n\n"
                                            is_in_complex_log = True
                                        elif is_in_complex_log and ('}' in line or ']' in line):
                                            llm_thoughts += f"⚙️ {line.strip()}\n\n"
                                            is_in_complex_log = False
                                        elif is_in_complex_log:
                                            llm_thoughts += f"⚙️ {line.strip()}\n\n"
                                        else:
                                            clean_lines.append(line)
                                    display_text = '\n'.join(clean_lines)
                                    
                                    # 渲染过滤后的正式回复
                                    message_placeholder.markdown(display_text.strip() + " ▌")
                                    
                                    # 将 LLM 内部思考追加到思考折叠框中
                                    if llm_thoughts:
                                        combined_thought = thought_content + "\n\n---\n**🧠 模型内部思考:**\n" + llm_thoughts
                                        think_placeholder.markdown(combined_thought)
                                    else:
                                        if thought_content:
                                            think_placeholder.markdown(thought_content)
                                    
                                # 处理工具调用 (追加到思考过程)
                                elif data.get("type") == "tool_start":
                                    tool_name = data.get("tool")
                                    # 更新 status 的标题
                                    think_status.update(label=f"🛠️ 正在调用工具: {tool_name}...", state="running")
                                    thought_content += f"\n\n**🛠️ 调用工具**: `{tool_name}`\n"
                                    think_placeholder.markdown(thought_content)
                                        
                                elif data.get("type") == "tool_end":
                                    tool_name = data.get("tool")
                                    output = data.get("output", "")
                                    # 尝试解析 COMPLEX 乱码并格式化显示
                                    if output.startswith("COMPLEX["):
                                        try:
                                            import ast
                                            queries = ast.literal_eval(output[7:])
                                            formatted_output = "🔍 **并行执行多个子查询:**\n"
                                            for idx, q in enumerate(queries):
                                                formatted_output += f"- {idx+1}. `{q[0]}`\n"
                                            thought_content += f"**✅ {tool_name} 执行完毕**\n{formatted_output}\n---\n"
                                        except:
                                            thought_content += f"**✅ {tool_name} 执行完毕**\n_由于输出过长已折叠_\n---\n"
                                    else:
                                        thought_content += f"**✅ {tool_name} 执行完毕**\n_由于输出过长已折叠_\n---\n"
                                    think_placeholder.markdown(thought_content)
                                    
                                # 处理提取的知识记录
                                elif data.get("type") == "knowledge_extracted":
                                    extracted_content = data.get("content", "")
                                    # 提取核心事实，去掉开头的 "-> 任务[xxx]的调查结论：" 等前缀，使其更清爽
                                    clean_content = extracted_content
                                    if "的调查结论：" in clean_content:
                                        clean_content = clean_content.split("的调查结论：\n")[-1]
                                    
                                    # 用一个绿色的高亮框展示提炼出的知识
                                    thought_content += f"\n\n🟢 **知识提炼成功:**\n```text\n{clean_content.strip()}\n```\n---\n"
                                    think_placeholder.markdown(thought_content)
                                        
                                elif data.get("type") == "reflection_log":
                                    think_status.update(label="🧠 正在进行自我反思...", state="running")
                                    # 追加反思日志到思考过程
                                    thought_content += f"\n\n**🧠 反思分析**: {data.get('analysis')}\n"
                                    thought_content += f"**下一步策略**: {data.get('feedback')}\n"
                                    think_placeholder.markdown(thought_content)
                                        
                                elif data.get("type") == "planner_log":
                                    think_status.update(label="📋 正在制定执行计划...", state="running")
                                    # 追加计划到思考过程
                                    plan = data.get("plan", [])
                                    thought_content += "\n\n**📋 执行计划**:\n"
                                    for i, task in enumerate(plan):
                                        thought_content += f"{i+1}. {task}\n"
                                    think_placeholder.markdown(thought_content)
                                    
                                elif data.get("type") == "end":
                                    # 任务完成，更新状态并收起面板
                                    think_status.update(label="✅ 任务执行完毕", state="complete", expanded=False)
                                    break
                                    
                                elif data.get("type") == "error":
                                    think_status.update(label="❌ 执行发生错误", state="error", expanded=True)
                                    st.error(f"发生错误: {data.get('error')}")
                                    break
                                    
                            except websockets.exceptions.ConnectionClosed:
                                break
                except Exception as e:
                    st.error(f"WebSocket 连接失败: {str(e)}")
                    
                return local_full_response

            # 在 Streamlit 的同步环境中运行异步的 WebSocket 客户端
            full_response = asyncio.run(connect_and_stream())
            
            # 最终渲染（去掉光标）
            message_placeholder.markdown(full_response)
            
            # 将复杂的日志格式化后一并保存在消息中，使其支持刷新后继续显示
            if "logs" not in st.session_state:
                st.session_state.logs = {}
                
            # 保存 AI 回复到历史
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"连接错误: {str(e)}")
