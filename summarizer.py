from llm import llm

def summarizer_node(state):

    outputs = state["task_outputs"]

    combined = "\n\n".join(
        [
            f"{task}\n{result}"
            for task, result in outputs.items()
        ]
    )

    prompt = f"""
    Create professional final summary.

    {combined}
    """

    response = llm.invoke(prompt)

    return {
        "final_summary": response.content
    }