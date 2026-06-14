from langchain_groq import ChatGroq

from config import (
    GROQ_API_KEY,
    GROQ_MODEL
)

llm = ChatGroq(
    model=GROQ_MODEL,
    api_key=GROQ_API_KEY
)

response = llm.invoke(
    "Say hello in one sentence."
)

print(response.content)