 

from rag.retriever import retrieve_context

query = (
    "Notion pricing plans"
)

context = retrieve_context(query)

print(context[:2000])