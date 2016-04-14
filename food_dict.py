#!/usr/env/python3

import json

user_intake = {}
caloric_data ={'popsicle':45, 'yogurt':120, 'muesli':200, 'beets':70, 'sweet potato':180, 'matcha latte': 230, 'mixed vegetables': 120, 'butter':40 }




def calorie_count(cal_total=0):						
    
    food = ''
        
    food = input('Enter a food,  when finished enter q:')
            
        
    if food == 'q':
        return user_intake, cal_total

    if food not in caloric_data:
        add_item = input('That item is not in our database, enter  the item name:')
        add_calories = int(input('Enter the calories in this item:'))
        #count= int(input('Number of servings:'))
        caloric_data[add_item] = add_calories
        user_intake[add_item] = add_calories
    

    if food in caloric_data:
        count= int(input('Number of servings:'))
        user_intake[food] = count
 

    #print (calorie_total)   
    #print (" ,".join([food for food in user_intake]))
    for food, count in user_intake.items():
        cal_total += caloric_data[food] * count 






    with open('daily.json','w') as daily_file:
        json.dump(user_intake,daily_file)
        json.dump(cal_total, daily_file)

    if food != 'q':

        return  calorie_count(cal_total=cal_total)






print(calorie_count())




    #if __name__ == "__main__":
        #calorie_count()

 

