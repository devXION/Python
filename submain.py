import requests
from requests.exceptions import HTTPError
import json
import urllib
import sys
BASE_URL = 'https://pokeapi.co/api/v2/'

x = input("What pokemon are you searching for : ")




try:
    response = requests.get(f"{BASE_URL}/pokemon/" + x)
    response.raise_for_status()
except HTTPError as ex:
    if ex.response.status_code == 404:
        print('pokemon not found')
        sys.exit(1)
    else:
        raise ex



def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    # print(text)



aDict = response.json()

print("Pokemon : " + aDict['name'])
print('------')
print('ID', +aDict['id'])
print('------')
print('abilities:')
for item in aDict['abilities']:
    name = item["ability"]["name"]
    print(name)
print('------')


response = requests.get(aDict['location_area_encounters'])
data = response.json()
print('locations:')
for it in data:
    qk = it['location_area']['name']
    print(qk)







# for item in data:
