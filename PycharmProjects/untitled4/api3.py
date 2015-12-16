import requests
# import AttrDict
import pprint

url = 'http://api.football-data.org/v1/soccerseasons/?season=2015'

class ApiClient(object):
    def __init__(self, url, key):
        self.url = url
        self.key = key

response = requests.get(url)
response1 = response.json()

pprint.pprint(response)
pprint.pprint(response1)

response1 = ['year']

response1 = open['text.txt', 'w']