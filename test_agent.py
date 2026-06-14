from agents.intelligence_agent import (
    IntelligenceAgent
)

from reports_generator import save_report

agent = IntelligenceAgent()

report = agent.analyze_changes(
competitor_name="Notion",
current_snapshot=
"snapshots/Notion_pricing.txt"
)   

file = save_report(
    "Notion",
    report
)

print(report)

print(
    f"Saved to {file}"
)