
import asyncio
import time
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.runnables.config import RunnableConfig
from langchain_core.callbacks import BaseCallbackHandler

# Custom Handler to measure duration
class LatencyCheckHandler(BaseCallbackHandler):
    def __init__(self):
        self.starts = {}
        self.ends = {}
        
    def on_chain_start(self, serialized, inputs, *, run_id, parent_run_id=None, **kwargs):
        name = serialized.get("name") if serialized else "Unknown"
        # LangGraph nodes often show up as 'LangGraph' or the node name if configured
        # But specifically we want to see if the node execution (Chain) is captured
        print(f"[START] {name} (ID: {run_id})")
        self.starts[run_id] = time.time()

    def on_chain_end(self, outputs, *, run_id, parent_run_id=None, **kwargs):
        end_time = time.time()
        start_time = self.starts.get(run_id)
        if start_time:
            duration = end_time - start_time
            print(f"[END] (ID: {run_id}) Duration: {duration:.4f}s")
        else:
            print(f"[END] (ID: {run_id}) NO START FOUND")

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# Define a node that sleeps
async def sleeping_node(state: State, config: RunnableConfig):
    print("--- Node is sleeping for 2 seconds ---")
    await asyncio.sleep(2)
    return {"messages": [HumanMessage(content="Slept")]}

def get_graph():
    workflow = StateGraph(State)
    workflow.add_node("sleeper", sleeping_node)
    workflow.add_edge(START, "sleeper")
    workflow.add_edge("sleeper", END)
    return workflow.compile()

async def main():
    app = get_graph()
    handler = LatencyCheckHandler()
    
    print("Running graph with sleep node...")
    await app.ainvoke(
        {"messages": [HumanMessage(content="hi")]},
        config={"callbacks": [handler], "run_name": "TestGraph"}
    )

if __name__ == "__main__":
    asyncio.run(main())
