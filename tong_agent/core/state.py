from typing import Annotated, TypedDict, Literal, Optional
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
import operator

class AgentState(TypedDict):
    """
    Agent 的状态定义 (Cursor-like Architecture)。
    """
    # 基础消息历史
    messages: Annotated[list[BaseMessage], add_messages]
    
    # 编辑器/环境上下文
    editor_context: Optional[str]
    
    # 意图与执行状态
    current_intent: Optional[str]
    selected_tool: Optional[str]
    execution_result: Optional[str]
    
    # 反思与控制流
    reflection: Optional[str]
    feedback_instruction: Optional[str]  # 新增：AI 生成的具体反馈指令
    retry_count: int
    step_count: int # ReAct 循环步数熔断器
    eval_count: int # 评估者驳回次数
    evaluator_approved: bool # 评估者是否通过
    next_action: Literal["finish", "retry", "reselect_tool", "ask_user", "continue", "max_retry"]
    
    # 长期记忆 (Long-term Memory)
    summary: Optional[str]
    retrieved_memories: Optional[str] # 新增：检索到的长期记忆
    working_memory: Annotated[list[str], operator.add] # 新增：工作记忆，用于存储当前任务中读取到的关键片段，防止长循环遗忘

    # 自适应规划器 (Adaptive Planner) 状态
    complexity: Optional[str] # "SIMPLE" 或 "COMPLEX"
    plan: Optional[list[str]] # 规划的任务列表
    current_task_idx: Optional[int] # 当前执行到第几个任务
    gathered_knowledge: Annotated[list[str], operator.add] # 【新增】逐步累积的纯净知识
    recent_search_queries: Annotated[list[str], operator.add] # 新增：用于防泥潭机制的搜索历史记录
