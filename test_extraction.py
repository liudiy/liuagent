import asyncio
import os
from langchain_openai import ChatOpenAI
from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import retrieve_middleware_docs

async def main():
    print("1. Running RAG tool...")
    rag_result = await retrieve_middleware_docs.ainvoke({"query": "TongHttpServer 的官方定义、集群架构要求及最低硬件配置"})
    
    print("\n--- RAG Result Length ---")
    print(len(rag_result))
    
    print("\n2. Truncating for qwen-turbo...")
    # 模拟 graph.py 中的截断，之前是 3000
    truncated_result = rag_result[:3000]
    print(f"Truncated Length: {len(truncated_result)}")
    
    print("\n3. Running qwen-turbo extraction...")
    llm_turbo = ChatOpenAI(
        model="qwen-turbo",
        temperature=0.1,
        api_key=os.environ.get("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
    
    current_task = "检索 TongHttpServer 的官方定义、集群架构要求及最低硬件配置"
    
    extract_prompt = f"""
    你是一个知识提炼助手。请根据以下【工具检索结果】，提取出对完成【当前子任务】有用的核心事实。
    要求：
    1. 尽量简短精炼，只保留事实、定义、架构要求或配置参数。
    2. 如果工具结果中没有提到有用的信息，请直接回复“未找到相关信息”。
    3. 严禁你自己编造知识。
    
    【当前子任务】：{current_task}
    【工具检索结果】：
    {truncated_result}
    """
    
    extracted = llm_turbo.invoke(extract_prompt).content.strip()
    print("\n--- Extracted Knowledge ---")
    print(extracted)

if __name__ == "__main__":
    asyncio.run(main())
