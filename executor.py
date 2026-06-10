from llm import llm

def execute_node(state):

    tasks = state["tasks"]

    completed = state["completed_tasks"]

    outputs = state["task_outputs"]

    next_task = None

    for task in tasks:

        if task not in completed:

            next_task = task
            break

    if not next_task:
        return state

    previous_context = "\n".join(
        [f"{k}:{v}" for k, v in outputs.items()]
    )

    prompt = f"""
    USER GOAL:
    {state['user_goal']}

    DOCUMENT CONTEXT:
    {state['retrieved_context']}

    PREVIOUS OUTPUTS:
    {previous_context}

    CURRENT TASK:
    {next_task}

    Execute current task only.
    """

    response = llm.invoke(prompt)

    outputs[next_task] = response.content

    completed.append(next_task)

    return {
        "completed_tasks": completed,
        "task_outputs": outputs,
        "current_task": next_task
    }