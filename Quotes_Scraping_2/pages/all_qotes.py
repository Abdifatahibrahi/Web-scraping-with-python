
from bs4 import BeautifulSoup
from locators import quotes_page_locators
from parsers.quotes_parser import QuoteParser


class QuotesPage:

    def __init__(self, page_content):
        self.page = BeautifulSoup(page_content, 'html.parser')

    
    @property
    def quotes(self):
        locator = quotes_page_locators.PAGE
        page_quotes = self.page.select(locator)
        return [QuoteParser(e) for e in page_quotes]

