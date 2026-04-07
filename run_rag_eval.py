import os
import sys
import asyncio
from dotenv import load_dotenv

sys.path.append(os.path.dirname(__file__))

from langchain_core.messages import HumanMessage
from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    ContextualPrecisionMetric,  # 检索精准度
    ContextualRecallMetric,     # 上下文召回率
    FaithfulnessMetric,         # 事实忠实度
    AnswerRelevancyMetric,      # 回答相关性
)

# 导入裁判和 Agent Graph
from tong_agent.sub_agents.rag_agent.eval_config import QwenEvalLLM, generate_manual_testset
from tong_agent.graph import get_graph  # <--- 直接导入 Agent

load_dotenv()


async def run_evaluation():
    print("🚀 开始运行 RAG 自动化评估 (DeepEval + Qwen)...")
    print("🤖 正在初始化 Agent Graph...")
    
    # 编译 Agent，准备上战场
    agent_app = get_graph()

    # 1. 准备评估模型 (Judge)
    judge_llm = QwenEvalLLM() 

    # 2. 准备指标 (Metrics)
    metrics = [
            ContextualRecallMetric(model=judge_llm, threshold=0.5),
            ContextualPrecisionMetric(model=judge_llm, threshold=0.5),
            FaithfulnessMetric(model=judge_llm, threshold=0.5),
            AnswerRelevancyMetric(model=judge_llm, threshold=0.5),
    ]

    # 3. 准备测试数据
    test_data = generate_manual_testset()
    print(f"📦 正在处理 {len(test_data)} 个测试用例...")
    test_cases = []
        

    for item in test_data:
        query = item["input"]
        expected_answer = item.get("expected_output")
        print(f"\n--------------------------------------------------")
        print(f"🎮 [测试用例] 正在提问: {query}")

        inputs = {"messages": [HumanMessage(content=query)]}
        try:
            
            final_state = await agent_app.ainvoke(inputs)
            messages = final_state["messages"]
            actual_output =  messages[-1].content
            print(f"🤖 [Agent 回答]: {actual_output[:100]}...") # 只打印前100字预览

            retrieval_context =[]
            for message in messages:
                if message.type == "tool" and message.name=="retrieve_middleware_docs":
                    retrieval_context.append(message.content)
            
            if not retrieval_context:
                print("⚠️ 测试用例 {query} 未触发检索工具")
                retrieval_context = ["Agent 未执行检索步骤。"]
                continue
            else:
                print(f"✅ [检索成功] 找到了 {len(retrieval_context)} 条检索记录。")
            
            test_case = LLMTestCase(
                input=query,
                actual_output=actual_output,
                expected_output=expected_answer,
                retrieval_context=retrieval_context,
            )
            test_cases.append(test_case)

        except Exception as e:
            print(f"⚠️ 测试用例 {query} 执行出错: {str(e)}")
            continue


    # [新增] 4. 提交给裁判打分
    print("\n⚖️  正在调用 DeepEval 进行打分，请稍候...")
    results = evaluate(test_cases, metrics)
    
    print("\n✅ 评估完成！")
    return results

# [新增] 程序入口
if __name__ == "__main__":
    try:
        asyncio.run(run_evaluation())
    except TypeError as e:
        if "print_results" in str(e):
             print("\n⚠️ 警告: 当前 DeepEval 版本不支持 print_results 参数，尝试移除该参数重试...")
             # 重新运行 evaluate，去掉 print_results
             # 这里无法直接获取上下文变量，所以只能建议用户手动修改
             print("❌ 请手动修改 run_rag_eval.py，将 evaluate(..., print_results=True) 改为 evaluate(...)")
        else:
            raise e





