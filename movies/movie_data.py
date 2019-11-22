# import requests 
# import json
# from pprint import pprint as pp

# kobis_key = "25f58e315e6e5146b438a1ee1f0c6cd9"

# def kobis(key, date):
#     base_URL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?"
#     get_URL = "key={}&targetDt={}&weekGb=0".format(key, date)
#     return base_URL + get_URL  

# def get_boxdata(date):
#     k_url = kobis(kobis_key, date)
#     res = requests.get(k_url).json()
#     # print(res['boxOfficeResult']['weeklyBoxOfficeList'])
#     boxdata = res.get('boxOfficeResult').get('weeklyBoxOfficeList')
#     # boxdata : 10개의 딕셔너리를 원소로 가지는 리스트
#     return boxdata 

# pp(get_boxdata(20090506))
