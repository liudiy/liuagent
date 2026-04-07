import os
from langchain_core.tools import tool
from openai import OpenAI

@tool
def aliyun_web_search(query: str) -> str:
    """
    使用阿里云 DashScope 的 Qwen 模型进行联网搜索。
    当用户询问实时的、互联网上的信息（如最新新闻、天气、技术文档等）时调用此工具。
    
    Args:
        query: 搜索关键词或问题。
        
    Returns:
        搜索结果的摘要或答案。
    """
    print(f"[Tool: aliyun_web_search] Searching for: {query}")
    
    api_key = os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        return "Error: DASHSCOPE_API_KEY environment variable not set."

    # 使用 OpenAI 兼容接口调用 DashScope
    # 文档参考：https://help.aliyun.com/zh/model-studio/web-search
    client = OpenAI(
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    try:
        # 使用 qwen-turbo 模型并开启 enable_search
        # 优化：改用 turbo 模型以提升速度，修改 Prompt 要求只返回摘要列表
        completion = client.chat.completions.create(
            model="qwen-turbo", # 降级为 Turbo，速度更快
            messages=[
                {'role': 'system', 'content': '你是一个高效的搜索助手。请搜索以下内容，并以【要点列表】的形式返回关键事实摘要。严禁长篇论述，严禁废话，直接罗列信息点。'},
                {'role': 'user', 'content': query}
            ],
            extra_body={"enable_search": True} 
        )
        
        return completion.choices[0].message.content

    except Exception as e:
        return f"Error during web search: {str(e)}"
