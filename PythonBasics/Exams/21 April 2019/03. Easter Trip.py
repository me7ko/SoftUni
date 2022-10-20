price = 0

destination = input()
date = input()
nights_count = int(input())


if destination == "France":
    if date == "21-23":
        price += 30
    elif date == "24-27":
        price += 35
    elif date == "28-31":
        price += 40

elif destination == "Italy":
    if date == "21-23":
        price += 28
    elif date == "24-27":
        price += 32
    elif date == "28-31":
        price += 39

if destination == "Germany":
    if date == "21-23":
        price += 32
    elif date == "24-27":
        price += 37
    elif date == "28-31":
        price += 43

total = nights_count * price
print(f"Easter trip to {destination} : {total:.2f} leva.")