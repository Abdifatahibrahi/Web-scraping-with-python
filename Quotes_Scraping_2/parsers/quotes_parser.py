from locators import quotes_locators  

class QuoteParser():
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Quote: {self.content} by {self.author}"

    @property
    def content(self):
        locator = quotes_locators.CONTENT
        return self.parent.select_one(locator).string


    @property
    def author(self):
        locator = quotes_locators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = quotes_locators.TAGS
        return self.parent.select_one(locator).string