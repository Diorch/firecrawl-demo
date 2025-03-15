from firecrawl.firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="")

# Scrape a website:
scrape_status = app.scrape_url(
  'https://firecrawl.dev', 
  params={'formats': ['markdown', 'html']}
)
with open('scrape_status.json', 'w') as file:
    file.write(str(scrape_status))

# Crawl a website:
# crawl_status = app.crawl_url(
#   'https://firecrawl.dev', 
#   params={
#     'limit': 100, 
#     'scrapeOptions': {'formats': ['markdown', 'html']}
#   },
#   poll_interval=30
# )
# import os

# with open('crawl_status.txt', 'w') as file:
#     file.write(str(crawl_status))