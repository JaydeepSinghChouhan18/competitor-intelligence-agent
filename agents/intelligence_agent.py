from langchain_groq import ChatGroq

from config import GROQ_API_KEY, GROQ_MODEL
from rag.retriever import retrieve_context


class IntelligenceAgent:

    def __init__(self):
        self.llm = ChatGroq(
            model=GROQ_MODEL,
            api_key=GROQ_API_KEY
        )

    def load_text_file(self, filepath):
        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:
            return f.read()

    def analyze_changes(
        self,
        competitor_name,
        current_snapshot
    ):

        current_text = self.load_text_file(
            current_snapshot
        )

        historical_context = retrieve_context(
            f"{competitor_name} pricing features positioning"
        )

        prompt = f"""
You are a professional competitor intelligence analyst.

Competitor:
{competitor_name}

Historical Information:
{historical_context}

Current Website Snapshot:
{current_text}

Analyze:

1. Pricing Changes
2. Feature Changes
3. Product Positioning Changes
4. Messaging Changes
5. Marketing Strategy Changes

Only mention meaningful changes.

Provide:

Executive Summary

Major Changes

Business Impact

Recommended Actions
"""

        response = self.llm.invoke(prompt)

        return response.content