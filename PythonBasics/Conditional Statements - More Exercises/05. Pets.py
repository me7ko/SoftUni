import math

days = int(input())
left_food_per_kg = int(input())
food_per_day_dog = float(input())
food_per_day_cat = float(input())
food_per_day_turtle = float(input())

total_food = (days * food_per_day_dog) + (days * food_per_day_cat) + (days * food_per_day_turtle / 1000)

if total_food <= left_food_per_kg:
    diff = math.floor(abs(left_food_per_kg - total_food))
    print(f"{diff} kilos of food left.")
else:
    diff = math.ceil(abs(left_food_per_kg - total_food))
    print(f"{diff} more kilos of food are needed.")
