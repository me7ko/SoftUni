budget = float(input())
season = input()

car = ""
car_class = ""
price = 0

if season == "Summer":
    car = "Cabrio"
    if budget <= 100:
        car_class = "Economy class"
        price = budget * 0.35
    elif 100 < budget <= 500:
        car_class = "Compact class"
        price = budget * 0.45
    else:
        car_class = "Luxury class"
        car = "Jeep"
        price = budget * 0.9
elif season == "Winter":
    car = "Jeep"
    if budget <= 100:
        car_class = "Economy class"
        price = budget * 0.65
    elif 100 < budget <= 500:
        car_class = "Compact class"
        price = budget * 0.8
    else:
        car_class = "Luxury class"
        car = "Jeep"
        price = budget * 0.9

print(car_class)
print(f"{car} - {price:.2f}")