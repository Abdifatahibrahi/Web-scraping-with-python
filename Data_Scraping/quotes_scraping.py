import requests

r = requests.get('https://quotes.toscrape.com/')
html = r.text

# with open('quotes.txt', 'w') as q:
#     for line  in html.split('\n'):
#         if '<span class="text" itemprop="text">' in line:
#             quotes = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '').strip()
#             q.write(quotes)
#             q.write('\n')


with open('authors.txt', 'w') as q:
    for line in html.split('\n'):
        if '<span>by <small class="author" itemprop="author">' in line:
            authors = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '').strip()
            
            q.write(authors)
            q.write('\n')
