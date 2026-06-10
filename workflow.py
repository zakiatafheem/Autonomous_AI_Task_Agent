from langgraph.graph import StateGraph, END

from state import AgentState

from planner import planner_node
from executor import execute_node
from summarizer import summarizer_node

def should_continue(state):

    if len(state["tasks"]) == len(
        state["completed_tasks"]
    ):
        return "summarize"

    return "execute"

def build_graph():

    workflow = StateGraph(AgentState)

    workflow.add_node(
        "planner",
        planner_node
    )

    workflow.add_node(
        "execute",
        execute_node
    )

    workflow.add_node(
        "summarize",
        summarizer_node
    )

    workflow.set_entry_point(
        "planner"
    )

    workflow.add_edge(
        "planner",
        "execute"
    )

    workflow.add_conditional_edges(
        "execute",
        should_continue,
        {
            "execute":"execute",
            "summarize":"summarize"
        }
    )

    workflow.add_edge(
        "summarize",
        END
    )

    return workflow.compile()