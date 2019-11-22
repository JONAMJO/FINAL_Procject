import requests
import csv
​
HEADERS = {'X-Naver-Client-Id': 'NqFdUzeArXgskeGxNaY7', 'X-Naver-Client-Secret': 'Cjr_blZwsy'}
​
movie = {}
with open('name.csv', newline = '', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie.update({row['movieNm']: row['movieNm']})
​
new_res = []
for cd, nm in movie.items():
​
    url = f'https://openapi.naver.com/v1/search/movie.json?query={nm}&display=1'
​
    response = requests.get(url, headers = HEADERS).json()
    res_item = response.get('items')[0]
​
    set_item = {}
    set_item['movieNm'] = res_item['movieNm']
    set_item['link'] = res_item['link']
    set_item['image'] = res_item['image']
    set_item['subtitle'] = res_item['subtitle']
    set_item['pubDate'] = res_item['pubDate']
    set_item['director'] = res_item['director']
    set_item['actor'] = res_item['actor']
    set_item['userRating'] = res_item['userRating']
​
    new_res.append(set_item)
​
from pprint import pprint
pprint(new_res)
