inherited_money = float(input())
living_year = int(input())

age = 17

for year in range(1800, living_year + 1):
    age += 1
    if year % 2 == 0:
        inherited_money -= 12000
    else:
        inherited_money -= 12000 + (50 * age)

if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    diff = abs(inherited_money)
    print(f"He will need {diff:.2f} dollars to survive.")