from langchain_core.runnables.config import RunnableConfig
from tong_agent.core.state import AgentState
from tong_agent.core.llm_factory import get_model
from tong_agent.core.logger import logger
import json

def planner_node(state: AgentState, config: RunnableConfig):
    """为复杂任务生成执行步骤"""
    logger.info("--- [Node: Planner] 制定复杂任务执行计划 ---")
    user_input = state["messages"][0].content
    
    prompt = f"""
    你是一个资深的分析师和规划专家。为了完成用户的复杂请求，请将其拆解为 2-4 个独立的子任务。
    
    【通用复杂问题拆解法则 (WBS)】：
    1. **独立探查 (Isolated Probe)**：如果涉及多个组件或技术（如 THS、TongWeb、TongRDS），为每个组件生成一个独立的检索任务，确保它们可以并行执行，互不干扰。
    2. **微观穿透 (Micro-Drilldown)**：要求寻找具体的配置参数、文件路径等落地细节。
    
    请以 JSON 数组格式返回计划列表，不要输出任何其他文本，只输出合法的 JSON 数组。
    例如：["搜索并总结 THS 的 SSL 配置方法", "搜索并总结 TongWeb 的 SSL 配置方法", "搜索并总结 TongRDS 的 SSL 配置方法"]
    
    用户请求：{user_input}
    """
    
    llm_plus = get_model(config, temp=0.2)
    
    plan_json_str = llm_plus.invoke(prompt, config=config).content.strip()
    # 移除可能存在的 Markdown 代码块标记
    if plan_json_str.startswith("```json"):
        plan_json_str = plan_json_str[7:-3].strip()
    elif plan_json_str.startswith("```"):
        plan_json_str = plan_json_str[3:-3].strip()
        
    try:
        plan_list = json.loads(plan_json_str)
        logger.info(f"--- [Planner] 制定了 {len(plan_list)} 步并行计划: {plan_list} ---")
        return {"plan": plan_list, "current_task_idx": 0}
    except Exception as e:
        logger.error(f"--- [Planner] JSON解析失败: {e} ---")
        return {"plan": [user_input], "current_task_idx": 0}
