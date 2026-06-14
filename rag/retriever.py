from rag.vectordb import get_vector_db


def retrieve_context(
        query,
        k=3):

    db = get_vector_db()

    results = db.similarity_search(
        query,
        k=k
    )

    context = []

    for doc in results:

        context.append(
            doc.page_content[:3000]
        )

    return "\n\n".join(context)