import os
import json
import pytest
from dotenv import load_dotenv

# Ensure we use the correct LLM for evaluation (Qwen-Turbo)
os.environ["OPENAI_API_KEY"] = os.environ.get("DASHSCOPE_API_KEY", "")
os.environ["OPENAI_BASE_URL"] = "https://dashscope.aliyuncs.com/compatible-mode/v1"

from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import HallucinationMetric, AnswerRelevancyMetric, FaithfulnessMetric
from deepeval.models.llms.openai_model import GPTModel

# --- Custom Model Wrapper for DeepEval ---
class QwenJudgeModel(GPTModel):
    def __init__(self):
        super().__init__(model="qwen-turbo")
        
# Initialize the metrics
qwen_model = QwenJudgeModel()
hallucination_metric = HallucinationMetric(threshold=0.1, model=qwen_model) # 越低越好，0表示无幻觉，设置0.1表示极低容忍度
answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.9, model=qwen_model) # 越高越好，设置0.9表示要求极高相关性
faithfulness_metric = FaithfulnessMetric(threshold=0.9, model=qwen_model) # 越高越好，设置0.9表示要求极其忠实于检索内容

# --- Load Test Data ---
def load_test_cases(limit=5):
    with open("RAG_Full_Evaluation_Results_v3.json", "r", encoding="utf-8") as f:
        data = json.load(f)["results"]
    
    # 注入序号以便在测试中打印
    for i, item in enumerate(data[:limit]):
        item["_index"] = i + 1
        item["_total"] = min(limit, len(data))
        
    return data[:limit]

test_data = load_test_cases(limit=5)

output_file = "deepeval_results.json"
if os.path.exists(output_file):
    try:
        os.remove(output_file)
    except Exception:
       import asyncio
import uuid
import os
import json

# Set mem0 testing flag before importing any TongAgent modules
os.environ["MEM0_TESTING_MODE"] = "True"
os.environ["QDRANT_PATH"] = ":memory:" # Force Qdrant into memory mode if possible

# --- Agent Import ---
import asyncio
import uuid
from tong_agent.graph import get_graph
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage
from mem0 import Memory
import httpx

# --- Helper Function to Invoke Agent ---
async def ainvoke_agent(question: str):
    # 每个并发任务需要独立的 memory 和 graph 实例
    memory = MemorySaver()
    agent_graph = get_graph(checkpointer=memory)
    
    # 每次调用生成唯一的 thread_id 防止并发冲突
    thread_id = f"test_deepeval_{uuid.uuid4().hex[:8]}"
    config = {"configurable": {"thread_id": thread_id}}
    
    # To get a clean agent answer without internal streaming artifacts,
    # let's just get the final state from the checkpointer or the final output of the graph.
    final_state = await agent_graph.ainvoke(
        {"messages": [HumanMessage(content=question)]},
        config
    )
    
    # Extract the last AIMessage from the final state
    messages = final_state.get("messages", [])
    if messages:
        agent_answer = messages[-1].content
    else:
        agent_answer = ""
        
    # Extract tool outputs from the message history for context
    retrieval_context = []
    for msg in messages:
        if getattr(msg, "type", "") == "tool" and msg.name in ["retrieve_middleware_docs", "rag_search", "aliyun_web_search"]:
            retrieval_context.append(str(msg.content))
            
    # Clean up the agent answer to remove <thought_process> if the model leaked it
    import re
    agent_answer = re.sub(r'<thought_process>.*?</thought_process>', '', agent_answer, flags=re.DOTALL).strip()
    
    return agent_answer, retrieval_context

# --- Pytest Parametrized Test ---
@pytest.mark.asyncio
@pytest.mark.parametrize("case_data", test_data)
async def test_rag_agent(case_data):
    question = case_data["question"]
    current_idx = case_data.get("_index", "?")
    total_idx = case_data.get("_total", "?")
    
    print(f"\n[{current_idx}/{total_idx}] 开始评测问题: {question}")
    
    # 动态调用 Agent 获取结果
    # Disable Mem0 completely for tests to avoid Qdrant / SQLite multi-processing issues
    os.environ["MEM0_TESTING_MODE"] = "True"
    os.environ["DISABLE_MEM0"] = "True"
    
    actual_output, retrieval_context = await ainvoke_agent(question)
    
    if not retrieval_context:
        # 如果检索为空，填充一个空字符串避免 deepeval 报错，或使用默认文本
        retrieval_context = [""]
        
    test_case = LLMTestCase(
        input=question,
        actual_output=actual_output,
        context=retrieval_context,
        retrieval_context=retrieval_context,
    )
    
    # We don't use assert_test directly because it throws AssertionError on failure
    # Instead, we measure the metrics manually to safely capture the scores
    metrics_results = []
    
    for metric in [hallucination_metric, answer_relevancy_metric, faithfulness_metric]:
        try:
            # Manually trigger the measurement
            metric.measure(test_case)
            metrics_results.append({
                "metric_name": metric.__class__.__name__,
                "score": metric.score,
                "reason": metric.reason,
                "passed": metric.is_successful()
            })
        except Exception as e:
            metrics_results.append({
                "metric_name": metric.__class__.__name__,
                "score": None,
                "reason": f"Error during measurement: {str(e)}",
                "passed": False
            })

    result_data = {
        "question": question,
        "agent_answer": actual_output,
        "metrics": metrics_results,
        "overall_passed": all(m["passed"] for m in metrics_results)
    }

    # Save the result to a local JSON file
    output_file = "deepeval_results.json"

    # Append to JSON file
    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as f:
            try:
                all_results = json.load(f)
            except json.JSONDecodeError:
                all_results = []
    else:
        all_results = []
        
    all_results.append(result_data)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    print("Run this file using: deepeval test run evaluate_with_deepeval.py")