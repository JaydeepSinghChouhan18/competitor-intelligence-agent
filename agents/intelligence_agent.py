from langchain_groq import ChatGroq
from config import GROQ_API_KEY, GROQ_MODEL
from tools.scraper import fetch_website_text

class IntelligenceAgent:

    def __init__(self):
        self.llm = ChatGroq(
            model=GROQ_MODEL,
            api_key=GROQ_API_KEY
        )

    def analyze_changes(self, competitor_name, url):

        current_text = fetch_website_text(url)

        prompt = f"""
You are a competitor intelligence analyst.

Competitor: {competitor_name}

Website Content:
{current_text}

Analyze:

1. Pricing strategy
2. Features
3. Positioning
4. Messaging
5. Marketing strategy

Give:
- Executive Summary
- Key Changes
- Business Impact
- Recommendations
"""

        response = self.llm.invoke(prompt)
        return response.content