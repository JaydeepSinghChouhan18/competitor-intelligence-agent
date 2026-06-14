from datetime import datetime
import json
from pathlib import Path

from playwright.sync_api import sync_playwright

from tools.parser import extract_visible_text
from tools.screenshot import build_screenshot_path


class WebsiteCrawler:

    def __init__(self):
        Path("snapshots").mkdir(exist_ok=True)
        Path("screenshots").mkdir(exist_ok=True)

    def crawl_page(
        self,
        competitor_name,
        url,
        page_type
    ):

        print(f"\nCrawling {competitor_name} - {page_type}")

        browser = None

        try:
            with sync_playwright() as p:

                browser = p.chromium.launch(
                    headless=True
                )

                page = browser.new_page(
                    viewport={
                        "width": 1440,
                        "height": 3000
                    }
                )

                page.goto(
                    url,
                    wait_until="networkidle",
                    timeout=120000
                )

                page.wait_for_timeout(3000)

                html = page.content()

                text = extract_visible_text(
                    html
                )

                screenshot_path = (
                    build_screenshot_path(
                        competitor_name,
                        page_type
                    )
                )

                page.screenshot(
                    path=screenshot_path,
                    full_page=True
                )

                timestamp = datetime.now().strftime(
                    "%Y%m%d_%H%M%S"
                )

                snapshot_file = (
                    f"snapshots/"
                    f"{competitor_name}_"
                    f"{page_type}_"
                    f"{timestamp}.txt"
                )

                with open(
                    snapshot_file,
                    "w",
                    encoding="utf-8"
                ) as f:
                    f.write(text)

                print(
                    f"Saved snapshot: "
                    f"{snapshot_file}"
                )

                print(
                    f"Saved screenshot: "
                    f"{screenshot_path}"
                )

                return {
                    "competitor": competitor_name,
                    "page_type": page_type,
                    "url": url,
                    "snapshot": snapshot_file,
                    "screenshot": screenshot_path
                }

        except Exception as e:

            print(
                f"Error crawling "
                f"{competitor_name} "
                f"{page_type}: {e}"
            )

            return None

        finally:

            if browser:
                browser.close()

    def crawl_competitors(
        self,
        competitors_file
    ):

        results = []

        with open(
            competitors_file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        competitors = data["competitors"]

        for competitor in competitors:

            name = competitor["name"]

            homepage_result = self.crawl_page(
                name,
                competitor["homepage"],
                "homepage"
            )

            pricing_result = self.crawl_page(
                name,
                competitor["pricing"],
                "pricing"
            )

            if homepage_result:
                results.append(
                    homepage_result
                )

            if pricing_result:
                results.append(
                    pricing_result
                )

        return results