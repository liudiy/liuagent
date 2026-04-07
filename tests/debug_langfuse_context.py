
import asyncio
import os
import uuid
from typing import Annotated, TypedDict, Any
from langchain_core.messages import HumanMessage, BaseMessage
from langchain_core.runnables import RunnableConfig
from langchain_core.callbacks import BaseCallbackHandler
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI

# ==========================================
# 1. Custom Debug Handler
# ==========================================
class DebugTraceHandler(BaseCallbackHandler):
    def __init__(self):
        self.runs = {} # id -> {name, parent_id}
        
    def on_chain_start(self, serialized: dict[str, Any], inputs: dict[str, Any], *, run_id, parent_run_id=None, **kwargs):
        name = serialized.get("name", "Unknown Chain") if serialized else "Unknown Chain"
        print(f"[DEBUG] Chain Start: {name} (ID={run_id}, Parent={parent_run_id})")
        self.runs[run_id] = {"name": name, "parent": parent_run_id, "type": "chain"}

    def on_chat_model_start(self, serialized: dict[str, Any], messages: list[list[BaseMessage]], *, run_id, parent_run_id=None, **kwargs):
        print(f"[DEBUG] Chat Model Start: (ID={run_id}, Parent={parent_run_id})")
        self.runs[run_id] = {"name": "ChatModel", "parent": parent_run_id, "type": "llm"}
        
    def on_tool_start(self, serialized: dict[str, Any], input_str: str, *, run_id, parent_run_id=None, **kwargs):
        print(f"[DEBUG] Tool Start: (ID={run_id}, Parent={parent_run_id})")
        self.runs[run_id] = {"name": "Tool", "parent": parent_run_id, "type": "tool"}

# ==========================================
# 2. Mock Graph Definition
# ==========================================
class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

async def node_with_llm(state: AgentState, config: RunnableConfig):
    print(f"--- Node Execution (Config ID: {config.get('run_id')}) ---")
    
    # 模拟 LLM 调用
    # 注意：这里我们使用一个 Mock LLM 或者真实的 ChatOpenAI (会失败但能触发回调)
    # 为了测试回调，我们必须让 invoke 发生
    llm = ChatOpenAI(api_key="sk-mock-key", temperature=0)
    
    try:
        # 关键点：这里必须传入 config
        print("--- Invoking LLM with config ---")
        await llm.ainvoke([HumanMessage(content="hello")], config=config)
    except Exception as e:
        print(f"LLM Error (Expected): {e}")
        
    return {"messages": [HumanMessage(content="response")]}

def get_test_graph():
    workflow = StateGraph(AgentState)
    workflow.add_node("node_a", node_with_llm)
    workflow.add_edge(START, "node_a")
    workflow.add_edge("node_a", END)
    return workflow.compile()

# ==========================================
# 3. Test Runner
# ==========================================
async def main():
    print(">>> Starting Trace Propagation Test <<<")
    
    debug_handler = DebugTraceHandler()
    app = get_test_graph()
    
    # 构造 Config，模拟 server.py 中的用法
    config = {
        "configurable": {"thread_id": "test_thread"},
        "callbacks": [debug_handler],
        "run_name": "Root Graph Run"
    }
    
    inputs = {"messages": [HumanMessage(content="hi")]}
    
    print("\n[Action] Invoking Graph...")
    await app.ainvoke(inputs, config=config)
    
    print("\n>>> Analysis <<<")
    # 1. 检查是否有 Root Run
    root_runs = [rid for rid, info in debug_handler.runs.items() if info["parent"] is None]
    print(f"Root Runs: {len(root_runs)} (IDs: {root_runs})")
    
    if not root_runs:
        print("❌ FAIL: No root run detected.")
        return

    root_id = root_runs[0]
    
    # 2. 检查是否有 LLM Run
    llm_runs = [rid for rid, info in debug_handler.runs.items() if info["type"] == "llm"]
    print(f"LLM Runs: {len(llm_runs)} (IDs: {llm_runs})")
    
    if not llm_runs:
        print("❌ FAIL: No LLM run detected.")
        return
        
    # 3. 检查连接性
    # Graph Execution -> Node Execution -> LLM Execution
    # 我们期望 LLM 的 parent 是 Node，Node 的 parent 是 Graph
    
    for llm_id in llm_runs:
        parent_id = debug_handler.runs[llm_id]["parent"]
        print(f"LLM ({llm_id}) Parent: {parent_id}")
        
        if parent_id:
            grandparent_id = debug_handler.runs[parent_id]["parent"]
            print(f"LLM Parent's Parent: {grandparent_id}")
            
            if grandparent_id == root_id or parent_id == root_id:
                 print("✅ SUCCESS: Trace is connected!")
            else:
                 print("⚠️ WARNING: Trace might be disconnected or deeper than expected.")
        else:
            print("❌ FAIL: LLM Run is an orphan (No parent).")

if __name__ == "__main__":
    asyncio.run(main())
