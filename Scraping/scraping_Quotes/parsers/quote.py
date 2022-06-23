from locators.quote_locators import QuoteLocators


class QuoteParser:
    
    def __init__(self, parent):
        self.parent = parent
        
    def __repr__(self):
        return f"<Quote: {self.content} by {self.author}"
        
    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        content = self.parent.select_one(locator).string
        return content
    
    
    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        author = self.parent.select_one(locator).string
        return author
    
    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        tags = [t.string for t in self.parent.select(locator)]
        return tags