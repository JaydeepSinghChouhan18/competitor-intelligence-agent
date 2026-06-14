from pathlib import Path


def build_screenshot_path(
        competitor_name,
        page_type):

    Path("screenshots").mkdir(
        exist_ok=True
    )

    return (
        f"screenshots/"
        f"{competitor_name}_{page_type}.png"
    )