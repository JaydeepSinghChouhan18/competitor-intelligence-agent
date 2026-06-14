from bs4 import BeautifulSoup


def extract_visible_text(html_content):
    soup = BeautifulSoup(html_content, "lxml")

    for tag in soup([
        "script",
        "style",
        "noscript",
        "svg",
        "iframe"
    ]):
        tag.decompose()

    text = soup.get_text(separator="\n")

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    return "\n".join(lines)
