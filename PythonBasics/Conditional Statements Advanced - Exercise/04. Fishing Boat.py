budget = int(input())
season = input()
fishermen_count = int(input())

rent = 0

if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

if fishermen_count <= 6:
    rent *= 0.9
elif 7 <= fishermen_count <= 11:
    rent *= 0.85
else:
    rent *= 0.75

if fishermen_count % 2 == 0 and season != "Autumn":
    rent *= 0.95

diff = abs(budget - rent)

if budget >= rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
