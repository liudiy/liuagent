import os
import json
import asyncio
import uuid
import re
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 设置 LLM API Key (如果需要使用 Qwen-Turbo 作为 Judge)
os.environ["OPENAI_API_KEY"] = os.environ.get("DASHSCOPE_API_KEY", "")
os.environ["OPENAI_BASE_URL"] = "https://dashscope.aliyuncs.com/compatible-mode/v1"
os.environ["MEM0_TESTING_MODE"] = "True"
os.environ["DISABLE_MEM0"] = "True"
os.environ["QDRANT_PATH"] = ":memory:"

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from tong_agent.graph import get_graph
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage

# ==========================================
# 1. 代理调用辅助函数
# ==========================================
async def ainvoke_agent(question: str):
    memory = MemorySaver()
    agent_graph = get_graph(checkpointer=memory)
    thread_id = f"test_custom_eval_{uuid.uuid4().hex[:8]}"
    config = {"configurable": {"thread_id": thread_id}}
    
    final_state = await agent_graph.ainvoke(
        {"messages": [HumanMessage(content=question)]},
        config
    )
    
    messages = final_state.get("messages", [])
    agent_answer = messages[-1].content if messages else ""
        
    retrieval_context = []
    for msg in messages:
        if getattr(msg, "type", "") == "tool" and msg.name in ["retrieve_middleware_docs", "rag_search", "aliyun_web_search"]:
            retrieval_context.append(str(msg.content))
            
    agent_answer = re.sub(r'<thought_process>.*?</thought_process>', '', agent_answer, flags=re.DOTALL).strip()
    return agent_answer, retrieval_context

# ==========================================
# 2. 自定义 LLM 评估器 (LLM as a Judge)
# ==========================================
class EvalResult(BaseModel):
    score: float = Field(description="评分，范围 0.0 到 1.0")
    reason: str = Field(description="给出该评分的详细原因和分析")

# 初始化裁判模型
judge_llm = ChatOpenAI(model="qwen-turbo", temperature=0).with_structured_output(EvalResult)

# 幻觉率 (Faithfulness) 提示词：评估回答是否完全基于检索到的上下文
faithfulness_prompt = PromptTemplate.from_template("""
你是一个严谨的评估专家。请评估给定的【回答】是否忠实于【检索上下文】。
【要求】:
1. 幻觉率是指【回答】中包含了【检索上下文】中没有的信息。
2. 如果【回答】完全由【检索上下文】支持，没有任何捏造、臆想或外部知识，给出 score = 1.0。
3. 如果【回答】包含部分未在上下文中出现的信息，给出 score = 0.5。
4. 如果【回答】完全与上下文无关或是凭空捏造的，给出 score = 0.0。
5. 忽略回答中的礼貌性用语。如果上下文为空，但回答也表示“不知道”或“无法回答”，则 score = 1.0（因为没有产生幻觉）。

【检索上下文】:
{context}

【回答】:
{answer}

请提供 score 和 reason。
""")

# 准确率/相关度 (Answer Relevancy) 提示词：评估回答是否解决了用户的问题
relevancy_prompt = PromptTemplate.from_template("""
你是一个严谨的评估专家。请评估给定的【回答】是否准确且相关地解答了【用户问题】。
【要求】:
1. 如果【回答】直接、准确、完整地解答了【用户问题】，给出 score = 1.0。
2. 如果【回答】相关但不够完整，或者包含大量冗余无关信息，给出 score = 0.5。
3. 如果【回答】完全没有解答【用户问题】，或者答非所问，给出 score = 0.0。
4. 如果回答表明“根据上下文无法回答”，且这确实是唯一合理的回复，请给出 score = 1.0（因为代理做出了正确的诚实反应）。

【用户问题】:
{question}

【回答】:
{answer}

请提供 score 和 reason。
""")

# ==========================================
# 3. 运行评估
# ==========================================
def load_test_cases(limit=5):
    with open("RAG_Full_Evaluation_Results_v3.json", "r", encoding="utf-8") as f:
        data = json.load(f)["results"]
    return data[:limit]

async def run_evaluation():
    print("🚀 开始自定义 Agent 评估测试...")
    test_cases = load_test_cases(5)
    total = len(test_cases)
    
    results = []
    
    for i, case in enumerate(test_cases):
        question = case["question"]
        print(f"\n[{i+1}/{total}] 正在测试问题: {question}")
        
        # 1. 调用 Agent
        print("  ⏳ 正在运行 Agent...")
        actual_output, retrieval_context = await ainvoke_agent(question)
        context_str = "\n\n".join(retrieval_context) if retrieval_context else "无上下文"
        
        # 2. 评估 Faithfulness (幻觉率的反面)
        print("  ⚖️ 正在评估 Faithfulness (忠实度/幻觉)...")
        try:
            faith_result = await judge_llm.ainvoke(faithfulness_prompt.format(context=context_str, answer=actual_output))
            faith_score = faith_result.score
            faith_reason = faith_result.reason
        except Exception as e:
            faith_score = 0.0
            faith_reason = f"评估失败: {e}"
            
        # 3. 评估 Answer Relevancy (准确率/相关度)
        print("  ⚖️ 正在评估 Answer Relevancy (准确率)...")
        try:
            rel_result = await judge_llm.ainvoke(relevancy_prompt.format(question=question, answer=actual_output))
            rel_score = rel_result.score
            rel_reason = rel_result.reason
        except Exception as e:
            rel_score = 0.0
            rel_reason = f"评估失败: {e}"
            
        print(f"  📊 结果 -> 忠实度: {faith_score} | 准确率: {rel_score}")
        print(f"  📝 理由 -> {rel_reason}")
        
        results.append({
            "question": question,
            "agent_answer": actual_output,
            "metrics": [
                {
                    "metric_name": "FaithfulnessMetric (No Hallucination)",
                    "score": faith_score,
                    "reason": faith_reason,
                    "passed": faith_score >= 0.8
                },
                {
                    "metric_name": "AnswerRelevancyMetric (Accuracy)",
                    "score": rel_score,
                    "reason": rel_reason,
                    "passed": rel_score >= 0.8
                }
            ],
            "overall_passed": faith_score >= 0.8 and rel_score >= 0.8
        })
        
    # 保存结果
    output_file = "custom_eval_results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
        
    print(f"\n✅ 测试完成！结果已保存至 {output_file}")
    
    # 打印总结
    passed_count = sum(1 for r in results if r["overall_passed"])
    print(f"📈 总通过率: {passed_count}/{total} ({(passed_count/total)*100:.1f}%)")

if __name__ == "__main__":
    asyncio.run(run_evaluation())
