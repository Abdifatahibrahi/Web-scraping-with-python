import requests



# with open('quotes.csv', 'a') as f:
#     for line in html.split('\n'):
#         print(line)
#         if '<span class="text" itemprop="text">“' in line:
#             quote = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '').strip()
            

#     for line in html.split('\n'):
#         # print(line)
#         if '<small class="author" itemprop="author">' in line:
#             author = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '').strip()
            
#             f.write(author +','+ quote)
#             f.write('\n')

for i in range(1,4):
    url = f'https://www.espncricinfo.com/latest-cricket-news?page={i}'
    r = requests.get(url)
    html = r.text
    print(html)