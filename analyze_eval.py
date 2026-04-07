import json

def analyze_results(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return

    failed_cases = [d for d in data.get('results', []) if not d.get('judge_is_accurate', True)]
    
    cat1_retrieval_miss = []
    cat2_false_refusal = []
    cat3_hallucination = []
    cat4_other = []

    for case in failed_cases:
        reason = case.get('judge_reasoning', '').lower()
        if case.get('judge_has_hallucination', False):
            cat3_hallucination.append(case)
        elif 'correctly refused' in reason or 'not found in the provided context' in reason or 'lack of relevant information' in reason or 'does not contain information' in reason or 'does not provide information' in reason:
            cat1_retrieval_miss.append(case)
        elif 'incorrect because the context contains' in reason or '上下文中确实包含' in reason or '上下文中存在' in reason or '文档中确实' in reason or '实际上可以从上下文中找到' in reason or 'information is present in the context' in reason or 'context does contain relevant information' in reason or 'could be used to address' in reason:
            cat2_false_refusal.append(case)
        else:
            cat4_other.append(case)

    print(f"Total Failed: {len(failed_cases)}")
    print(f"1. Retrieval Miss (Agent correctly refused, but answer expected): {len(cat1_retrieval_miss)}")
    print(f"2. False Refusal (Agent refused despite context having answer): {len(cat2_false_refusal)}")
    print(f"3. Hallucination (Agent made up facts): {len(cat3_hallucination)}")
    print(f"4. Other: {len(cat4_other)}")
    
    if cat4_other:
        print("\nOther cases:")
        for c in cat4_other:
            print(f"Q: {c['question']}\nReason: {c['judge_reasoning']}")

if __name__ == "__main__":
    analyze_results("RAG_Full_Evaluation_Results_v2.json")
