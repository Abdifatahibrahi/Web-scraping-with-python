import requests
import json


with open('news.csv', 'a') as f:
    for i in range(1,5):
        print(f"Page: {i}")
        url = f'https://hs-consumer-api.espncricinfo.com/v1/edition/feed?edition=pk&lang=en&page={i}&records=10'
        res = requests.get(url)

        data = json.loads(res.text)
        news = data['results']
        for new in news:
            f.write(new['id'] +', '+ new['title'] +', '+ new['cardType'] )
            f.write('\n')
        
