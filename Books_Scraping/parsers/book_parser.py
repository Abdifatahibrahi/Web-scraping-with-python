import re

from locators.book_locators import BookLocators





class BookParser:

    def __init__(self, parent):
        self.parent = parent

    def __str__(self):
        return f"<Book {self.name}, {self.price}, with ({self.rating}) rating"


    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
        
    }


    @property
    def name(self):
        locator = BookLocators.Name_Locator
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = BookLocators.Link_Locator
        item_link = self.parent.select_one(locator).attrs['href']
        return item_link

    @property
    def rating(self):
        locator = BookLocators.Rating_Locator
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_class = [p for p in classes if p != 'star-rating']
        rated_number = BookParser.RATINGS.get(rating_class[0])
        return rated_number

    @property
    def price(self):
        locator = BookLocators.Price_Locator
        rate = self.parent.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'

        matcher = re.search(pattern, rate)

        
        return matcher.group(0)