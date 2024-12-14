import requests

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbrlawjsdlf131545002'

params = {
    'ttbkey': API_KEY,
    'QueryType': 'ItemNewSpecial',
    'MaxResults': 50,
    'OutPut': 'JS',
    'SearchTarget': 'Book',
    'Version': 20131101
}

datas = requests.get(API_URL,params=params).json() # item 키에 title / author / pubdate / ISBN 다 있다.
result = []

for data in datas['item']:
    res_dict = {}
    res_dict['제목'] = data['title']
    res_dict['저자'] = data['author']
    res_dict['출간일'] = data['pubDate']
    res_dict['ISBN'] = data['isbn']
    result.append(res_dict)

# print(result)