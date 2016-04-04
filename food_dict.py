import json
foods = {}
calories ={'popsicle':45, 'yogurt':120, 'muesli':200, 'beets':70, 'sweet potato':180, 'matcha latte': 230, 'mixed vegetables': 120, 'butter':40 }


def calorie_count():						
    while True:
        food = input('Enter a food(q for quit):')
        if food == 'q':
            break
        count= int(input('Count:'))
        foods[food] = count
    print(" ,".join([food for food in foods]))

    total = 0
    for food, count in foods.items():
        if food in calories:
            total += calories[food] * count 
            print (total)
    return foods
    
    daily_file = open('daily.json','w')
    json.dump(foods,daily_file, indent=4)
    json.dump(total, daily_file, indent=4)
    daily_file.close()
calorie_count()


