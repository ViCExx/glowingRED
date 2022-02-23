import requests
import json
import pprint

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

for questions in response.json()['items']:
    print(questions['title'])
    print(questions['view_count'],("Views"))
    print()