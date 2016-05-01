#!/usr/env/python3

import json
import requests

payload = {'format':'json','q':'butter','sort':'r','max':'3','offset':'0','api_key':'nASa7zKM8QMfmzIYG3e3G0lsyyLIP94H23IlHqAK'} 


r = requests.get('http://api.nal.usda.gov/ndb/search/', params = payload)
r  = r.json()
print(json.dumps(r, indent=4, sort_keys=True))

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

