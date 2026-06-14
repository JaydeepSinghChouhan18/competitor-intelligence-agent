import streamlit as st
from agents.intelligence_agent import IntelligenceAgent

st.title("🚀 Competitor Intelligence SaaS")

competitor = st.text_input("Competitor Name")
url = st.text_input("Competitor Website URL")

if st.button("Analyze"):
    agent = IntelligenceAgent()

    report = agent.analyze_changes(
        competitor_name=competitor,
        url=url
    )

    st.subheader("Report")
    st.write(report)