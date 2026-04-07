
import os
import asyncio
from typing import Annotated, TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.runnables.config import RunnableConfig
from langfuse.callback import CallbackHandler

# 1. Mock Environment
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-1234567890" # Dummy, just to init handler if needed, or rely on mock
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-1234567890"
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"

# 2. Define Graph
class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

async def node_a(state: State, config: RunnableConfig):
    print("--- Node A ---")
    # Simulate LLM call with config
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key="sk-mock")
    # We expect this to fail auth but trigger callbacks
    try:
        await llm.ainvoke([HumanMessage(content="Hi")], config=config)
    except Exception as e:
        print(f"LLM Call A failed as expected (Mock): {e}")
    return {"messages": [HumanMessage(content="Node A Done")]}

async def node_b(state: State, config: RunnableConfig):
    print("--- Node B ---")
    return {"messages": [HumanMessage(content="Node B Done")]}

workflow = StateGraph(State)
workflow.add_node("node_a", node_a)
workflow.add_node("node_b", node_b)
workflow.add_edge(START, "node_a")
workflow.add_edge("node_a", "node_b")
workflow.add_edge("node_b", END)
app = workflow.compile()

# 3. Test Execution
async def run_test():
    print("Initializing Handler...")
    # We will use a mock handler to see what methods are called
    # But to test Langfuse logic, we'd need real credentials. 
    # Instead, let's verify that the 'config' is propagating callbacks.
    
    # Create a custom callback to intercept events
    from langchain_core.callbacks import BaseCallbackHandler
    class TestHandler(BaseCallbackHandler):
        def __init__(self):
            self.starts = []
            self.ends = []
            
        def on_chain_start(self, serialized, inputs, **kwargs):
            id = kwargs.get("run_id")
            parent = kwargs.get("parent_run_id")
            name = serialized.get("name") if serialized else "Unknown"
            print(f"Start Chain: {name} (ID: {id}, Parent: {parent})")
            self.starts.append({"id": id, "parent": parent, "type": "chain"})

        def on_chat_model_start(self, serialized, messages, **kwargs):
            id = kwargs.get("run_id")
            parent = kwargs.get("parent_run_id")
            print(f"Start ChatModel: (ID: {id}, Parent: {parent})")
            self.starts.append({"id": id, "parent": parent, "type": "llm"})

    handler = TestHandler()
    
    print("Running Graph...")
    await app.ainvoke(
        {"messages": [HumanMessage(content="Start")]},
        config={"callbacks": [handler]}
    )
    
    print("\n--- Trace Analysis ---")
    # Verify we have a root and children
    if not handler.starts:
        print("FAIL: No events captured.")
        return

    root = handler.starts[0]
    print(f"Root: {root}")
    
    children = [s for s in handler.starts if s["parent"] == root["id"]]
    print(f"Direct Children of Root: {len(children)}")
    
    grand_children = []
    for child in children:
        g_kids = [s for s in handler.starts if s["parent"] == child["id"]]
        grand_children.extend(g_kids)
    print(f"Grand Children: {len(grand_children)}")

    # Check if LLM call inside Node A had a parent
    llm_starts = [s for s in handler.starts if s["type"] == "llm"]
    for llm in llm_starts:
        if llm["parent"]:
            print(f"SUCCESS: LLM call {llm['id']} has parent {llm['parent']}")
        else:
            print(f"FAIL: LLM call {llm['id']} has NO parent (Orphan Trace)")

if __name__ == "__main__":
    asyncio.run(run_test())
