import re
from locators import books_locators

class BookParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Book: {self.title} worth {self.price} has {self.rating} stars"

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }


    @property
    def title(self):
        locator = books_locators.TITLE
        item = self.parent.select_one(locator)
        item_title = item.attrs['title']
        return item_title

    @property
    def link(self):
        locator = books_locators.LINK
        item = self.parent.select_one(locator)
        item_link = item.attrs['href']
        return item_link

    @property
    def price(self):
        locator = books_locators.PRICE
        item = self.parent.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item)

        return matcher.group(1)

    @property
    def rating(self):
        locator = books_locators.RATING
        item = self.parent.select_one(locator)
        classes = [c for c in item.attrs['class']]
        rating_c = [p for p in classes if p != 'star-rating']
        integer_rating = BookParser.RATINGS.get(rating_c[0])
        return integer_rating