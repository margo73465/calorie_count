import json
import requests


API_key = '65f3c1d9a1d3c6f7edcf2802023fe069'
API_id = '7f0a2caa'

payload_s = {'fields':['item_name','2Citem_id','2Cbrand_name','2Cnf_calories', '2Cnftotal_fat'],'appId':'7f0a2caa','appKey':'65f3c1d9a1d3c6f7edcf2802023fe069'}
r_search = requests.get('https://api.nutritionix.com/v1_1/search/{beets}', params=payload_s)
r_search = r_search.json()
print(json.dumps(r_search, indent=4, sort_keys=True))

def hits():
    for item in 'hits':
        if item in 'fields'[1] == 'USDA':
            print (item)
hits() 
