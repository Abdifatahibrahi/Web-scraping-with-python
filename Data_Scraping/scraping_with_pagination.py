import requests

for x in range(1, 11):
    print(f"Page: {x}")
    url = f'https://quotes.toscrape.com/page/{x}/'
    r = requests.get(url)
    html = r.text

    with open('authors.txt', 'a', encoding='utf-8') as f:
        for line in html.split('\n'):
            if '<span>by <small class="author" itemprop="author">' in line:
                authors = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '').strip()
                f.write(authors)
                f.write("\n")
