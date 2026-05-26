# streamlit_app.py

import os
import json
import streamlit as st

from typing import TypedDict, List, Dict
from dotenv import load_dotenv

from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq


load_dotenv()

# PAGE CONFIG

st.set_page_config(
    page_title="Autonomous Task Agent",
    page_icon="🤖",
    layout="wide"
)
# CSS
st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.stButton>button {
    width: 100%;
    height: 3rem;
    font-size: 18px;
    border-radius: 10px;
}

.task-box {
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    background-color: #1e1e1e;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.title("Autonomous AI Task Agent")

st.markdown("""
Multi-step autonomous AI workflow using:
- Groq LLM
- LangGraph
- Agentic AI
- Multi-step reasoning
""")
# LOAD LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0
)

# AGENT STATE
class AgentState(TypedDict):
    user_goal: str
    tasks: List[str]
    completed_tasks: List[str]
    task_outputs: Dict[str, str]
    current_task: str
    final_summary: str

# TASK PLANNER
def planner_node(state: AgentState):

    goal = state["user_goal"]

    prompt = f"""
    You are an autonomous AI planner.

    Your job is to create ONLY task steps
    related to the user's exact goal.

    USER GOAL:
    {goal}

    Rules:
    - Do NOT change the topic
    - Do NOT invent unrelated examples
    - Keep tasks highly relevant
    - Keep tasks sequential
    - Generate 3 to 5 tasks maximum

    Return ONLY valid JSON.

    Example format:

    {{
        "tasks": [
            "Research machine learning algorithms",
            "Explain supervised learning",
            "Explain unsupervised learning",
            "Compare major algorithms",
            "Generate final summary"
        ]
    }}
    """

    response = llm.invoke(prompt)

    try:

        parsed = json.loads(response.content)

        tasks = parsed["tasks"]

    except Exception:

        tasks = [
            "Understand user goal",
            "Research topic",
            "Generate final summary"
        ]

    return {
        "tasks": tasks
    }
# EXECUTOR NODE

def execute_node(state: AgentState):

    tasks = state["tasks"]
    completed = state["completed_tasks"]
    outputs = state["task_outputs"]

    next_task = None

    # Find next incomplete task
    for task in tasks:

        if task not in completed:

            next_task = task
            break

    if not next_task:
        return state

    previous_context = "\n".join([
        f"{k}: {v}"
        for k, v in outputs.items()
    ])

    prompt = f"""
    You are an autonomous AI execution agent.

    USER GOAL:
    {state['user_goal']}

    CURRENT TASK:
    {next_task}

    PREVIOUS CONTEXT:
    {previous_context}

    Rules:
    - Stay strictly related to the user's goal
    - Do NOT introduce unrelated topics
    - Use professional explanations
    - Be concise but informative

    Execute ONLY the current task.
    """

    try:

        response = llm.invoke(prompt)

        task_result = response.content

    except Exception as e:

        task_result = f"ERROR: {str(e)}"

    outputs[next_task] = task_result
    completed.append(next_task)

    return {
        "completed_tasks": completed,
        "task_outputs": outputs,
        "current_task": next_task
    }
# CONTINUE CONDITION
#
def should_continue(state: AgentState):

    if len(state["tasks"]) == len(state["completed_tasks"]):
        return "summarize"

    return "execute"

# FINAL SUMMARY NODE

def summarizer_node(state: AgentState):

    outputs = state["task_outputs"]

    combined_output = "\n\n".join([
        f"TASK: {task}\nOUTPUT:\n{result}"
        for task, result in outputs.items()
    ])

    prompt = f"""
    Create a professional final summary
    from the following outputs.

    {combined_output}
    """

    response = llm.invoke(prompt)

    return {
        "final_summary": response.content
    }

# BUILD GRAPH
workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_node)
workflow.add_node("execute", execute_node)
workflow.add_node("summarize", summarizer_node)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "execute")

workflow.add_conditional_edges(
    "execute",
    should_continue,
    {
        "execute": "execute",
        "summarize": "summarize"
    }
)

workflow.add_edge("summarize", END)

app = workflow.compile()

# USER INPUT

goal = st.text_area(
    "Enter Your Goal",
    height=150,
    #Example: Research AI startups in healthcare and generate insights
)


# RUN BUTTON
if st.button("🚀 Run Autonomous Agent"):

    if not goal.strip():

        st.warning("Please enter a goal.")

    else:

        with st.spinner("Agent is thinking..."):

            initial_state = {
                "user_goal": goal,
                "tasks": [],
                "completed_tasks": [],
                "task_outputs": {},
                "current_task": "",
                "final_summary": ""
            }

            result = app.invoke(initial_state)

        # DISPLAY TASKS

        #st.subheader("📌 Planned Tasks")

        #for i, task in enumerate(result["tasks"], start=1):

            #st.markdown(f"""
            #<div class="task-box">
            #    <b>Task {i}:</b> {task}
            #</div>
            #""", unsafe_allow_html=True)

        # DISPLAY TASK OUTPUTS

        st.subheader("⚙️ Task Outputs")

        for task, output in result["task_outputs"].items():

            with st.expander(task):

                st.write(output)

