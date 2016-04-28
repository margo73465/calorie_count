#!/usr/env/python3

import json
import requests

API_key = '65f3c1d9a1d3c6f7edcf2802023fe069'
API_id = '7f0a2c'
payload_s = {'results':'0:3','fields':'brand_name','appId': '7f0a2caa', 'appKey': '65f3c1d9a1d3c6f7edcf2802023fe069'}
payload_i = {'id':'513fceb575b8dbbc21001487','appId': '7f0a2caa', 'appKey': '65f3c1d9a1d3c6f7edcf2802023fe069'}
r_search = requests.get('https://api.nutritionix.com/v1_1/search/{beets}', params=payload_s) 
r_item = requests.get('https://api.nutritionix.com/v1_1/item', params=payload_i)
r_search = r_search.json()
r_item = r_item.json()
print (json.dumps(r_search, indent=4, sort_keys=True))
#print (json.dumps(r_item, indent=4, sort_keys=True))
for item in 'hits':
    if item in fields['brand_name'] == 'USDA':
        print (item) 




#food:servings dict
count_dict = {}
#food:calorie dict
user_intake = {}
caloric_data ={'popsicle':45, 'yogurt':120, 'muesli':200, 'beets':70, 'sweet potato':180, 
'matcha latte': 230, 'mixed vegetables': 120, 'butter':40 }


def calorie_count():						
    
    cal_total = 0
    food = input('Enter a food,  when finished enter q:')
    
    if food == 'q': 
        return user_intake
    
    if food != 'q':
        if food not in caloric_data:
            add_item = input('That item is not in our database, enter the item name:')
            add_calories = int(input('Enter the calories in this item:'))
            caloric_data[add_item] = add_calories
            user_intake[add_item] = add_calories
       
        #Get serving amount, look up user entered food in database and add food:calorie 
        #to user_intake, add food:serving to count_dict
        if food in caloric_data:
            count= int(input('Number of servings:'))
            user_intake[food] = caloric_data[food]
            count_dict[food] = count
            
        with open('daily.json','w') as daily_file:
            json.dump(user_intake,daily_file)
            json.dump(cal_total, daily_file)

    return calorie_count()

def cal_amount():
    cal_total = 0
    for food in user_intake:
        cal_total += user_intake[food] * count_dict[food]
    return cal_total


print(calorie_count(), cal_amount())




    #if __name__ == "__main__":
        #calorie_count() 

