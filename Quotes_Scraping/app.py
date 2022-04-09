import requests

from pages.quotes_page import QuotePage

page_content = requests.get('http://quotes.toscrape.com').content
page = QuotePage(page_content)

for quote in page.quotes:
    print(quote)

