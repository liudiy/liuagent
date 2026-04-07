import asyncio
from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import get_base_retrievers

async def main():
    print("Testing Parent-Child Retriever...")
    vector_retriever, bm25_retriever = get_base_retrievers()
    
    query = "TongHttpServer 的高可用配置"
    print(f"\nQuery: {query}")
    
    docs = vector_retriever.invoke(query)
    print(f"Retrieved {len(docs)} documents.")
    
    for i, doc in enumerate(docs[:3]):
        print(f"\n--- Doc {i+1} ---")
        print(f"Source: {doc.metadata.get('source', 'Unknown')}")
        print(f"Content length: {len(doc.page_content)}")
        print(f"Preview: {doc.page_content[:200]}...")

if __name__ == "__main__":
    asyncio.run(main())