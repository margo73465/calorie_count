import json
import requests

payload_s = {'fields': 'item_name,item_id,brand_name,nf_calories,nftotal_fat','appId':'7f0a2caa','appKey':'65f3c1d9a1d3c6f7edcf2802023fe069'}
r_search = requests.get('https://api.nutritionix.com/v1_1/search/beets', params=payload_s)
r_search = r_search.json()
print(json.dumps(r_search, indent=4, sort_keys=True))

 
