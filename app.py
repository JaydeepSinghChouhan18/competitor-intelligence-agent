import streamlit as st

from agents.intelligence_agent import IntelligenceAgent

st.title("Competitor Intelligence Agent")

competitor = st.text_input("Competitor Name")

snapshot_path = st.text_input(
    "Snapshot File Path",
    "snapshots/Notion_pricing.txt"
)

if st.button("Analyze"):

    agent = IntelligenceAgent()

    report = agent.analyze_changes(
        competitor_name=competitor,
        current_snapshot=snapshot_path
    )

    st.subheader("Analysis Report")
    st.write(report)