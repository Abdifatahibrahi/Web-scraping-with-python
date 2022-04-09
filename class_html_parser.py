import re

from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">$51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''

# soup = BeautifulSoup(ITEM_HTML, 'html.parser')

class ParsedItemLocator:


    Name_Locator = 'article h3 a'
    Link_Locator = 'article h3 a'
    Price_Locator = 'article.product_pod p.price_color'
    Rating_Locator = 'article.product_pod p.star-rating'

class ParsedItem:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocator.Name_Locator
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = ParsedItemLocator.Link_Locator
        item_link = self.soup.select_one(locator).attrs['href']
        return item_link

    @property
    def rating(self):
        locator = ParsedItemLocator.Rating_Locator
        paragraph = self.soup.select_one(locator)
        classes = paragraph.attrs['class']
        wanted_class = [p for p in classes if p != 'star-rating']
        return wanted_class[0]

    @property
    def price(self):
        locator = ParsedItemLocator.Price_Locator
        rate = self.soup.select_one(locator).string

        pattern = '$([0-9]+\.[0-9]+)'

        matcher = re.search(pattern, rate)

        
        return float(matcher.group(1))


    # find_item_name()
    # find_item_link()
    # find_item_rating()
    # find_rating()

item = ParsedItem(ITEM_HTML)
print(item.link)