import json

from llm import llm

def planner_node(state):

    goal = state["user_goal"]
    context = state["retrieved_context"]

    prompt = f"""
    You are an autonomous AI planner.

    USER GOAL:
    {goal}

    DOCUMENT CONTEXT:
    {context}

    Create 3-5 sequential tasks.

    Return valid JSON:

    {{
        "tasks":[]
    }}
    """

    response = llm.invoke(prompt)

    try:

        tasks = json.loads(
            response.content
        )["tasks"]

    except:

        tasks = [
            "Understand Goal",
            "Research Topic",
            "Generate Summary"
        ]

    return {
        "tasks": tasks
    }