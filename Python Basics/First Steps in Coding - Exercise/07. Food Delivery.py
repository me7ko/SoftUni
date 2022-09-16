chicken_meat = 10.35
menu_fish = 12.40
vegetarian_menu = 8.15
delivery_price = 2.50

ordered_chicken = int(input())
ordered_fish = int(input())
ordered_vegetarian = int(input())

sum = (ordered_chicken * chicken_meat) + (ordered_fish * menu_fish) + (ordered_vegetarian * vegetarian_menu)
dessert = sum * 0.2
total = round(sum + dessert + delivery_price, 2)
print(total)
