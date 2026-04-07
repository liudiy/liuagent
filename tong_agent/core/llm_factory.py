import os
from langchain_openai import ChatOpenAI
from langchain_core.runnables.config import RunnableConfig
from typing import Optional

def get_model(config: Optional[RunnableConfig] = None, model_name: str = "deepseek-chat", temp: float = 0.1):
    """统一初始化模型工厂"""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        print("Warning: DEEPSEEK_API_KEY not found.")
    
    model = ChatOpenAI(
        model=model_name,
        api_key=api_key,
        base_url="https://api.deepseek.com/v1",
        temperature=temp,
        streaming=True,
        max_retries=3,
        timeout=120,
    )
    return model

def get_fast_model(config: Optional[RunnableConfig] = None):
    """获取一个用于快速分类或提炼的轻量级模型"""
    api_key = os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        print("Warning: DASHSCOPE_API_KEY not found.")
        
    model = ChatOpenAI(
        model="qwen-turbo",
        temperature=0.0,
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    return model
