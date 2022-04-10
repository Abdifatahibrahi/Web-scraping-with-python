import re
from bs4 import BeautifulSoup

from locators.book_page_locators import PAGE, PAGER
from parsers.book_parser import BookParser

class AllBooks:
    def __init__(self, page_content):
        self.page = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        locator = PAGE
        page_item = self.page.select(locator)
        return [BookParser(b) for b in page_item]


    @property
    def page_count(self):
        locator = PAGER
        content = self.page.select_one(locator).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        match = re.search(pattern, content)

        page_no = int(match.group(1))
        return page_no

