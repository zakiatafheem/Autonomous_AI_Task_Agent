from typing import TypedDict, List, Dict

class AgentState(TypedDict):

    user_goal: str
    retrieved_context: str

    tasks: List[str]
    completed_tasks: List[str]

    task_outputs: Dict[str, str]

    current_task: str
    final_summary: str