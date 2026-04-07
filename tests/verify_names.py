
import asyncio
import time
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.runnables.config import RunnableConfig
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.runnables import RunnableLambda

# Custom Handler to verify names
class NameCheckHandler(BaseCallbackHandler):
    def on_chain_start(self, serialized, inputs, *, run_id, parent_run_id=None, **kwargs):
        name = serialized.get("name") if serialized else "Unknown"
        print(f"[START] Name: '{name}' (ID: {run_id})")

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def my_node(state: State):
    return {"messages": [HumanMessage(content="done")]}

def get_graph_with_names():
    workflow = StateGraph(State)
    
    # Wrap in RunnableLambda and set name
    node_runnable = RunnableLambda(my_node).with_config(run_name="MyCustomNodeName")
    
    workflow.add_node("node_a", node_runnable)
    workflow.add_edge(START, "node_a")
    workflow.add_edge("node_a", END)
    return workflow.compile()

async def main():
    app = get_graph_with_names()
    handler = NameCheckHandler()
    
    print("Running graph with named node...")
    await app.ainvoke(
        {"messages": [HumanMessage(content="hi")]},
        config={"callbacks": [handler]}
    )

if __name__ == "__main__":
    asyncio.run(main())
