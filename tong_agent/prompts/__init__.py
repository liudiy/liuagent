import os
from pathlib import Path

# 获取 prompts 文件夹的绝对路径
PROMPTS_DIR = Path(__file__).parent

def load_prompt(filename: str) -> str:
    """读取并返回对应的 Prompt 文件内容"""
    file_path = PROMPTS_DIR / filename
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error loading prompt {filename}: {e}")
        return ""

# 导出所有 Prompt
INTENT_PARSE_NODE_INSTRUCTION = load_prompt("intent_parse.md")
EVALUATOR_NODE_INSTRUCTION = load_prompt("evaluator.md")
SUMMARIZATION_NODE_INSTRUCTION = load_prompt("summarization.md")
GENERATE_RESPONSE_INSTRUCTION = load_prompt("generate_response.md")

__all__ = [
    "INTENT_PARSE_NODE_INSTRUCTION",
    "EVALUATOR_NODE_INSTRUCTION",
    "SUMMARIZATION_NODE_INSTRUCTION",
    "GENERATE_RESPONSE_INSTRUCTION"
]
