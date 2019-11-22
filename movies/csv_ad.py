import requests
import csv
from datetime import datetime, timedelta
​
def my_url(**kwargs):
    basic_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?'
    for key, value in kwargs.items():
           basic_url += f'{key}={value}&'
    
    return f'{basic_url}'
​
new_res_json = []
​
for i in range(20):
    dt = datetime(2019,7,13) - timedelta(weeks=i)
​
    api = {
        'key': '3f44dcd1f60bc37d709a2bdfbab207e6',
        'targetDt': dt.strftime('%Y%m%d'),
        'weekGb': '0'
    }
​
    res = requests.get(my_url(**api))
    res.json = res.json()
    res_json = res.json['boxOfficeResult']['weeklyBoxOfficeList']
​
    for j in range(len(res_json)):
        set_json = {}
        set_json['movieNm'] = res_json[j]['movieNm']
        new_res_json.append(set_json)
​
new2_res_json = list({k['movieNm']: k for k in new_res_json}.values())
​
with open(f'name.csv ', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movieNm', 'movieNm',)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
​
    for row in new2_res_json:
        writer.writerow(row)
