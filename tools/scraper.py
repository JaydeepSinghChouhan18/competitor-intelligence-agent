import requests
from bs4 import BeautifulSoup

def fetch_website_text(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(res.text, "html.parser")

    # remove scripts/styles
    for tag in soup(["script", "style"]):
        tag.extract()

    text = soup.get_text(separator="\n")
    return text[:12000]  # limit for LLM