import streamlit as st

from vector_store import build_vector_store
from retriever import retrieve_context

from workflow import build_graph

app = build_graph()

st.title("Autonomous AI Task Agent")

goal = st.text_area(
    "Enter Your Goal"
)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if st.button("Run Agent"):

    vectordb = build_vector_store(
        uploaded_file
    )

    retrieved_context = retrieve_context(
        goal,
        vectordb
    )

    state = {

        "user_goal": goal,

        "retrieved_context":
        retrieved_context,

        "tasks": [],

        "completed_tasks": [],

        "task_outputs": {},

        "current_task": "",

        "final_summary": ""
    }

    result = app.invoke(state)

    st.subheader("Task Outputs")

    for task, output in result[
        "task_outputs"
    ].items():

        with st.expander(task):
            st.write(output)

    st.subheader(
        "Final Summary"
    )

    st.success(
        result["final_summary"]
    )