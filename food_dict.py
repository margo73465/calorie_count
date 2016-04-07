#!/usr/env/python3

import json

user_intake = {}
caloric_data ={'popsicle':45, 'yogurt':120, 'muesli':200, 'beets':70, 'sweet potato':180, 'matcha latte': 230, 'mixed vegetables': 120, 'butter':40 }


def calorie_count():						
     food = ''
     while food != 'q':
        
        food = input('Enter a food,  when finished enter q:')
 
        if food == 'q':
            break
        
        if food not in caloric_data:
            add_item = input('That item is not in our database, enter  the item name:')
            add_calories = int(input('Enter the calories in this item:'))
            caloric_data[add_item] = add_calories
            user_intake[add_item] = add_calories
            
        if food in caloric_data:
            count= int(input('Number of servings:'))
            user_intake[food] = count
        
        
            
        print(" ,".join([food for food in user_intake]))
     
        for food, count in user_intake.items():
            calorie_total  = 0
            if food in caloric_data:
               calorie_total += caloric_data[food] * count 
               print (calorie_total)
        
        return user_intake
    
        with open('daily.json','w') as daily_file:
            json.dump(user_intake,daily_file)
            json.dump(calorie_total, daily_file)
   
#if __name__ == "main":
calorie_count()


