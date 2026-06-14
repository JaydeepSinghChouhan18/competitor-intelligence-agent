from tools.crawler import WebsiteCrawler

crawler = WebsiteCrawler()

results = crawler.crawl_competitors(
    "competitors.json"
)

for r in results:
    print(r)