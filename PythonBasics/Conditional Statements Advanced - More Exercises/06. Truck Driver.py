season = input()
km_per_month = float(input())
price = 0

if season in ["Spring", "Autumn"]:
    if km_per_month <= 5000:
        price = (km_per_month * 0.75) * 4
    elif 5000 < km_per_month <= 10000:
        price = (km_per_month * 0.95) * 4
    elif 10000 < km_per_month <= 20000:
        price = (km_per_month * 1.45) * 4

elif season == "Summer":
    if km_per_month <= 5000:
        price = (km_per_month * 0.9) * 4
    elif 5000 < km_per_month <= 10000:
        price = (km_per_month * 1.1) * 4
    elif 10000 < km_per_month <= 20000:
        price = (km_per_month * 1.45) * 4
elif season == "Winter":
    if km_per_month <= 5000:
        price = (km_per_month * 1.05) * 4
    elif 5000 < km_per_month <= 10000:
        price = (km_per_month * 1.25) * 4
    elif 10000 < km_per_month <= 20000:
        price = (km_per_month * 1.45) * 4


price_with_tax = price * 0.9
print(f"{price_with_tax:.2f}")