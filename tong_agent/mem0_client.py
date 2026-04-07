import os
from dotenv import load_dotenv
from mem0 import Memory

# Load environment variables
load_dotenv()

_mem0_client_instance = None

def get_mem0_client():
    """
    初始化 Mem0 客户端，配置 DeepSeek 作为 LLM，本地 HuggingFace 模型作为 Embedder
    使用单例模式避免多实例导致的 Qdrant 锁问题
    """
    global _mem0_client_instance
    
    # 检查是否禁用了 Mem0
    if os.environ.get("DISABLE_MEM0", "").lower() == "true":
        print("DEBUG: Mem0 is disabled via DISABLE_MEM0 environment variable.", flush=True)
        # 返回一个 Mock 客户端，避免报错
        class MockMem0:
            def search(self, *args, **kwargs): return []
            def get_all(self, *args, **kwargs): return []
            def add(self, *args, **kwargs): return None
        return MockMem0()

    if _mem0_client_instance is not None:
        return _mem0_client_instance

    # 获取本地模型绝对路径
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(current_dir, "models", "bge-small-zh-v1.5")
    
    # 确保存储目录存在
    storage_dir_name = os.environ.get("MEM0_STORAGE_PATH", "mem0_storage")
    storage_path = os.path.join(current_dir, storage_dir_name)
    if not os.path.exists(storage_path):
        os.makedirs(storage_path)

    print(f"DEBUG: Using storage path: {storage_path}", flush=True)

    config = {
        "llm": {
            "provider": "deepseek",
            "config": {
                "model": "deepseek-chat",
                "api_key": os.environ.get("DEEPSEEK_API_KEY"),
                "temperature": 0.1,
                "max_tokens": 1500
            }
        },
        "embedder": {
            "provider": "openai",
            "config": {
                "model": "text-embedding-v1",
                "openai_base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
                "api_key": os.environ.get("DASHSCOPE_API_KEY"),
                "embedding_dims": 1536
            }
        },
        "vector_store": {
            "provider": "qdrant",
            "config": {
                "collection_name": "mem0",
                "path": storage_path,
                "embedding_model_dims": 1536,
                "on_disk": True
            }
        },
        "version": "v1.1"
    }
    
    # Debug: Print config
    print(f"DEBUG: mem0 config: {config}", flush=True)
    
    try:
        _mem0_client_instance = Memory.from_config(config)
        return _mem0_client_instance
    except Exception as e:
        print(f"ERROR: Failed to create Memory from config: {e}", flush=True)
        raise
