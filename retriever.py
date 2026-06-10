def retrieve_context(query, vectordb):

    if vectordb is None:
        return ""

    docs = vectordb.similarity_search(
        query,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context