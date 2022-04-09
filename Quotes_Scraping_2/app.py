import requests

from pages.all_qotes import QuotesPage


page_content = requests.get('https://quotes.toscrape.com').content
page = QuotesPage(page_content)

quotes = page.quotes

for quote in quotes:
    print(quote)