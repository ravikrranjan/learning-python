import pprint
import requests
import json
res = requests.get('https://google.com')

# print(res.status_code)
# print(res.headers['Date'])
# print(res.text)

data = requests.get(
    'https://opentdb.com/api.php?amount=1&category=18&difficulty=easy&type=multiple')

print(data.text)
