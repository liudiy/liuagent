import json
import time
import os
import sys
from tqdm import tqdm
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import Literal

# Ensure the project root is in the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import retrieve_middleware_docs

# --- Pydantic Models for Output Parsing ---
class AgentResponse(BaseModel):
    thought_process: str = Field(description="你的内部思考过程：逐段检查 Context，寻找与问题相关的线索。")
    answer: str = Field(description="最终的回答内容...")
    refused: bool = Field(description="True if the agent refused to answer due to lack of information or irrelevant question. False otherwise.")

class JudgeEvaluation(BaseModel):
    is_accurate: bool = Field(description="True if the answer correctly addresses the question based on the context. False if it's wrong or missed key points.")
    has_hallucination: bool = Field(description="True if the answer contains information NOT present in the context (made up facts, fake parameters, etc.). False if strictly grounded.")
    reasoning: str = Field(description="Brief explanation of why these scores were given.")

# --- Initialization ---
def get_qwen_judge_llm(temperature=0.1):
    return ChatOpenAI(
        model="qwen-turbo", # Qwen acts as the impartial judge
        api_key=os.environ.get("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=temperature
    )

def get_deepseek_agent_llm(temperature=0.1):
    return ChatOpenAI(
        model="deepseek-chat", # Your actual agent uses DeepSeek
        api_key=os.environ.get("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com/v1",
        temperature=temperature
    )

def generate_agent_answer(query: str, context: str) -> AgentResponse:
    """Simulates the RAG Agent generating an answer based on retrieved context using DeepSeek."""
    llm = get_deepseek_agent_llm(temperature=0.1).with_structured_output(AgentResponse)
    
    prompt = PromptTemplate.from_template("""
你是一个极其严谨且极具解决问题能力的东方通（TongWeb, TongRDS, THS）资深底层架构师。
你的任务是：基于提供的 <Context> 来解答用户的 <Question>。

【最高指令】：
1. 请先在 thought_process 中一步步写下你的思考过程。仔细寻找隐藏在段落中间的配置项、原理或步骤。
2. 允许并鼓励你进行逻辑推演！如果用户问的是复杂的方案设计（如分配方案、断电重启顺序等），你应当根据 <Context> 中提供的零散配置项和基本原理，结合你的专业架构师经验，合理地将它们组合推演出最优方案，不要轻易拒答。
3. 事实必须有据可查！你可以推演架构，但绝对不能胡编乱造任何具体的端口号、配置文件路径或命令行参数。如果 <Context> 中完全没有提及相关的底层机制或参数，你才可以拒绝回答（设置 refused 为 true）。

<Context>
{context}
</Context>

<Question>
{query}
</Question>
    """)
    
    chain = prompt | llm
    try:
        return chain.invoke({"context": context, "query": query})
    except Exception as e:
        print(f"Error generating answer: {e}")
        return AgentResponse(thought_process="Error", answer=f"Error generating answer: {e}", refused=True)

def judge_answer(query: str, context: str, expected_intent: str, agent_response: AgentResponse) -> JudgeEvaluation:
    """Uses LLM as a Judge to evaluate the Agent's answer."""
    llm = get_qwen_judge_llm(temperature=0.1).with_structured_output(JudgeEvaluation)
    
    prompt = PromptTemplate.from_template("""
你是一个严苛的质量评测专家（LLM-as-a-Judge）。
你的任务是评估 RAG 系统的回答是否准确且没有幻觉。

【评测标准】：
1. **准确性 (is_accurate)**: 
   - 如果 expected_intent 是 'answer'：回答必须解决问题。如果拒绝回答但上下文中明明有答案，则为 False。
   - 如果 expected_intent 是 'reject'（陷阱题）：系统必须拒绝回答（refused=True）。如果它试图强答，则准确性为 False。
2. **幻觉 (has_hallucination)**:
   - 检查 Agent 的回答中是否包含了 <Context> 中根本没有提到的实体、数字、配置项或步骤。
   - 如果有，即使它在现实世界中是正确的，也必须判定为发生幻觉 (True)！
   - 如果 Agent 拒绝回答（refused=True），通常不算作幻觉 (False)。

<Question>
{query}
</Question>

<Expected_Intent>
{expected_intent} (answer: 应该回答; reject: 应该拒绝)
</Expected_Intent>

<Context_Provided_To_Agent>
{context}
</Context_Provided_To_Agent>

<Agent_Answer>
{answer}
(Refused Flag: {refused})
</Agent_Answer>
    """)
    
    chain = prompt | llm
    try:
        return chain.invoke({
            "query": query, 
            "context": context, 
            "expected_intent": expected_intent,
            "answer": agent_response.answer,
            "refused": agent_response.refused
        })
    except Exception as e:
        print(f"Error judging answer: {e}")
        return JudgeEvaluation(is_accurate=False, has_hallucination=False, reasoning=str(e))

def run_evaluation():
    with open('RAG测试集.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    test_cases = data.get("test_cases", [])
    print(f"Loaded {len(test_cases)} test cases for full evaluation.")
    
    results = []
    stats = {
        "total": len(test_cases),
        "accurate_count": 0,
        "hallucination_count": 0,
        "refused_correctly": 0,
        "failed_to_refuse": 0
    }
    
    for tc in tqdm(test_cases, desc="Evaluating 100 RAG Cases"):
        query = tc["question"]
        expected_intent = tc.get("expected_intent", "answer")
        
        try:
            # 1. Retrieve Context
            retrieval_start = time.time()
            context_raw = retrieve_middleware_docs.invoke({"query": query})
            context_str = str(context_raw)[:15000] # Limit context size to avoid token overflow
            retrieval_time = time.time() - retrieval_start
            
            # 2. Generate Answer
            agent_response = generate_agent_answer(query, context_str)
            
            # 3. Judge the Answer
            evaluation = judge_answer(query, context_str, expected_intent, agent_response)
            
            # 4. Update Stats
            if evaluation.is_accurate:
                stats["accurate_count"] += 1
            if evaluation.has_hallucination:
                stats["hallucination_count"] += 1
                
            if expected_intent == "reject":
                if agent_response.refused:
                    stats["refused_correctly"] += 1
                else:
                    stats["failed_to_refuse"] += 1
            
            # 5. Record Result
            results.append({
                "id": tc["id"],
                "category": tc["category"],
                "question": query,
                "expected_intent": expected_intent,
                "retrieval_time": round(retrieval_time, 2),
                "agent_answer": agent_response.answer,
                "agent_refused": agent_response.refused,
                "judge_is_accurate": evaluation.is_accurate,
                "judge_has_hallucination": evaluation.has_hallucination,
                "judge_reasoning": evaluation.reasoning
            })
            
        except Exception as e:
            print(f"\nError processing case {tc['id']}: {e}")
            results.append({
                "id": tc["id"],
                "error": str(e)
            })
            
        # Save intermediate results just in case it crashes midway
        with open('RAG_Full_Evaluation_Results.json', 'w', encoding='utf-8') as f:
            json.dump({"stats": stats, "results": results}, f, ensure_ascii=False, indent=4)
            
    # Calculate final percentages
    stats["accuracy_rate"] = f"{(stats['accurate_count'] / stats['total']) * 100:.2f}%"
    stats["hallucination_rate"] = f"{(stats['hallucination_count'] / stats['total']) * 100:.2f}%"
    
    output_file = 'RAG_Full_Evaluation_Results_v3.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({"stats": stats, "results": results}, f, ensure_ascii=False, indent=4)
        
    print("\n" + "="*50)
    print("🎉 FULL EVALUATION COMPLETE")
    print(f"Total Cases: {stats['total']}")
    print(f"Accuracy Rate: {stats['accuracy_rate']}")
    print(f"Hallucination Rate: {stats['hallucination_rate']}")
    print(f"Results saved to {output_file}")
    print("="*50)

if __name__ == "__main__":
    run_evaluation()
