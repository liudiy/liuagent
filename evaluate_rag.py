import json
import time
from tqdm import tqdm
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Ensure the project root is in the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tong_agent.sub_agents.rag_agent.tool.rag_tool_v2 import retrieve_middleware_docs

def evaluate_retrieval():
    # Load test cases
    with open('RAG测试集.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    test_cases = data.get("test_cases", [])
    print(f"Loaded {len(test_cases)} test cases.")
    
    results = []
    
    # We will just test the first 10 for a quick evaluation, or all 100 if we want.
    # Let's do 10 to make sure it works without timing out, then we can run full.
    # Actually, running 100 might take 10-20 minutes depending on LLM (Query Rewriting).
    # Let's run the first 5 of each category (15 total) for a quick smoke test.
    
    # Group by category
    categories = {}
    for tc in test_cases:
        cat = tc["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(tc)
        
    sample_cases = []
    for cat, cases in categories.items():
        sample_cases.extend(cases[:5]) # 5 from each category
        
    print(f"Running a smoke test on {len(sample_cases)} samples...")
    
    for tc in tqdm(sample_cases, desc="Evaluating RAG Retrieval"):
        query = tc["question"]
        try:
            start_time = time.time()
            # retrieve_middleware_docs is a LangChain tool, invoke it
            retrieved_docs_str = retrieve_middleware_docs.invoke({"query": query})
            elapsed = time.time() - start_time
            
            results.append({
                "id": tc["id"],
                "category": tc["category"],
                "question": query,
                "retrieved_context_length": len(retrieved_docs_str) if isinstance(retrieved_docs_str, str) else len(str(retrieved_docs_str)),
                "retrieved_context": str(retrieved_docs_str)[:500] + "..." if len(str(retrieved_docs_str)) > 500 else str(retrieved_docs_str),
                "time_seconds": round(elapsed, 2),
                "status": "success"
            })
        except Exception as e:
            results.append({
                "id": tc["id"],
                "category": tc["category"],
                "question": query,
                "status": "error",
                "error_msg": str(e)
            })
            
    # Save results
    with open('RAG_SmokeTest_Results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
        
    print("Smoke test complete. Results saved to RAG_SmokeTest_Results.json")

if __name__ == "__main__":
    evaluate_retrieval()
