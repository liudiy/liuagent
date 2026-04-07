
import sys
import os
import unittest
from unittest.mock import MagicMock

# 1. Mock dependencies BEFORE importing graph.py
# This prevents actual API calls or DB connections during the test
sys.modules["tong_agent.mem0_client"] = MagicMock()
sys.modules["tong_agent.sub_agents.rag_agent.tool.rag_tool_v2"] = MagicMock()
sys.modules["tong_agent.tools.aliyun_web_search"] = MagicMock()
sys.modules["tong_agent.tools.code_interpreter"] = MagicMock()
sys.modules["tong_agent.tools.server_tools"] = MagicMock()
sys.modules["tong_agent.tools.file_tools"] = MagicMock()
sys.modules["langchain_openai"] = MagicMock()

# Mock specific objects that graph.py expects
mock_chat_model = MagicMock()
# When invoke is called, return a fake response
mock_response = MagicMock()
mock_response.content = "Mock AI Response"
mock_response.tool_calls = []
mock_chat_model.invoke.return_value = mock_response
mock_chat_model.bind_tools.return_value = mock_chat_model
mock_chat_model.bind.return_value = mock_chat_model

sys.modules["langchain_openai"].ChatOpenAI.return_value = mock_chat_model

# Ensure we can import from project root
sys.path.append(os.getcwd())

# 2. Import the graph
# (We need to mock the tools list inside graph.py or ensure the mocks above handle it)
# The graph.py imports specific tools, so our sys.modules mocks should handle that.
try:
    from tong_agent.graph import get_graph
except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)

# 3. Setup Tracing Verification
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import HumanMessage
import asyncio
import time

class TraceVerifier(BaseCallbackHandler):
    def __init__(self):
        self.captured_nodes = {} # name -> {"start": time, "end": time}
        
    def on_chain_start(self, serialized, inputs, *, run_id, parent_run_id=None, **kwargs):
        # In the new RunnableLambda config, the name should appear in serialized['name'] 
        # or commonly in the 'name' attribute of the object.
        # LangChain's serialized dict usually has a 'name' key.
        name = serialized.get("name") if serialized else kwargs.get("name")
        
        # We are looking for our specific node names
        target_nodes = [
            "retrieve_memory_node", 
            "context_update_node", 
            "summarize_conversation_node", 
            "intent_parse_node",
            "tool_exec_node",
            "reflection_node",
            "generate_response_node"
        ]
        
        if name in target_nodes:
            print(f"✅ [TRACE START] Captured Node: {name}")
            self.captured_nodes[name] = {"start": time.time()}
        # else:
        #     print(f"   [TRACE IGNORE] {name}")

    def on_chain_end(self, outputs, *, run_id, parent_run_id=None, **kwargs):
        # We don't have name here directly usually, but we assume if start fired, end fires for same run_id
        # For simplicity in this mock test, we just want to see if the nodes run.
        pass

async def run_verification():
    print(">>> Starting Trace Verification <<<")
    verifier = TraceVerifier()
    
    # Initialize Graph
    graph = get_graph()
    
    # Run Graph with Config
    inputs = {"messages": [HumanMessage(content="Hello, testing tracing.")]}
    config = {
        "callbacks": [verifier],
        "run_name": "Test_Root_Run"
    }
    
    try:
        await graph.ainvoke(inputs, config=config)
    except Exception as e:
        print(f"Graph execution failed (expected due to mocks): {e}")
        # Even if it fails, we should have seen some nodes start
    
    print("\n>>> Verification Results <<<")
    # Check if we captured the critical nodes
    required_nodes = ["retrieve_memory_node", "context_update_node", "intent_parse_node"]
    
    success = True
    for node in required_nodes:
        if node in verifier.captured_nodes:
            print(f"✅ Node '{node}' was correctly traced with name.")
        else:
            print(f"❌ Node '{node}' was NOT traced or had wrong name.")
            success = False
            
    if success:
        print("\n🎉 SUCCESS: All key nodes are reporting their specific names to callbacks!")
        print("This means Langfuse will show these names and their individual latencies.")
    else:
        print("\n⚠️ FAILURE: Some nodes are missing names.")

if __name__ == "__main__":
    asyncio.run(run_verification())
