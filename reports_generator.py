from datetime import datetime
from pathlib import Path


def save_report(
        competitor_name,
        report_text):

    Path("reports").mkdir(
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"reports/"
        f"{competitor_name}_"
        f"{timestamp}.md"
    )

    with open(
            filename,
            "w",
            encoding="utf-8") as f:

        f.write(report_text)

    return filename