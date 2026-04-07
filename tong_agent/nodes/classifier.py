from langchain_core.runnables.config import RunnableConfig
from tong_agent.core.state import AgentState
from tong_agent.core.llm_factory import get_fast_model
from tong_agent.core.logger import logger

def classifier_node(state: AgentState, config: RunnableConfig):
    """判断任务类型：闲聊/基础概念、简单搜索、复杂规划"""
    logger.info("--- [Node: Classifier] 判断任务复杂度与意图 ---")
    user_input = state["messages"][0].content
    
    # 使用通用的意图分类 Prompt，不写死具体例子
    prompt = f"""
    作为智能路由节点，请分析用户的输入请求，并将其严格分类为以下三种类型之一（只输出 DIRECT、SIMPLE 或 COMPLEX）：

    - DIRECT: 纯粹的日常闲聊、问候或通用常识对话。这类请求不需要依赖任何外部工具、企业私有知识库或联网搜索，大模型直接回答即可。
    - SIMPLE: 明确且单一的专业问题或业务查询。通常只需要调用一次外部工具（如检索文档、查配置或报错）即可获得答案，具体调用什么工具由后续Agent自行决定。
    - COMPLEX: 复杂的综合性任务。这类问题包含多个子意图，需要跨多份资料对比、多步骤推理、或需要先制定计划分步执行（如集群架构规划）。
    
    请求：{user_input}
    """
    
    # 实例化一个轻量级的模型，专门用于快速分类
    llm_turbo = get_fast_model(config)
    
    # 调用模型得到结果
    result = llm_turbo.invoke(prompt, config=config).content.strip().upper()
    logger.info(f"--- [Classifier] 判断结果: {result} ---")
    
    # 确保返回这三种之一
    if "DIRECT" in result:
        complexity = "DIRECT"
    elif "COMPLEX" in result:
        complexity = "COMPLEX"
    else:
        complexity = "SIMPLE"
        
    return {"complexity": complexity}
