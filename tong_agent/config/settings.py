import os

class Settings:
    """
    集中化配置管理。
    生产环境中建议使用 pydantic_settings 的 BaseSettings 来自动加载 .env 文件，
    这里为了最简依赖，使用标准的 os.environ 封装。
    """
    # 通用配置
    DEFAULT_MODEL_NAME: str = os.getenv("DEFAULT_MODEL_NAME", "deepseek-r1")
    FAST_MODEL_NAME: str = os.getenv("FAST_MODEL_NAME", "deepseek-v3")
    
    # Mem0 配置
    DISABLE_MEM0: bool = os.getenv("DISABLE_MEM0", "false").lower() == "true"
    
    # 路径配置
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    PROMPTS_DIR: str = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "prompts")

settings = Settings()
