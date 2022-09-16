price_vegi = float(input())
price_fruits = float(input())
kilograms_vegi = int(input())
kilograms_fruits = int(input())

all_price = price_fruits * kilograms_fruits + price_vegi * kilograms_vegi

price_in_euro = all_price / 1.94

print(f"{price_in_euro:.2f}")