from bs4 import BeautifulSoup

simple_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<h1>This is a title</h1>
<p class="subtitle"> lorem ipsum dollar sit emet</p>
<p>Here is another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
    
</body>
</html>'''

simple_soup = BeautifulSoup(simple_html, 'html.parser')

def find_title():
    title = simple_soup.find('h1')
    print(title.string)

def find_paragraph():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)

def find_list():
    list_items = simple_soup.find_all('li')
    list_content = [item.string for item in list_items]
    print(list_content)


def without_p():
    paragraphs = simple_soup.find_all('p')
    other_p = [p.string for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_p)


without_p()

find_list()
find_title()

find_paragraph()