budget = float(input())
season = input()

locations = ""
place_to_stay = ""
price = 0

if season == "Summer":
    locations = "Alaska"
    if budget <= 1000:
        place_to_stay = "Camp"
        price = budget * 0.65
    elif 1000 < budget <= 3000:
        place_to_stay = "Hut"
        price = budget * 0.8
    else:
        place_to_stay = "Hotel"
        price = budget * 0.9
elif season == "Winter":
    locations = "Morocco"
    if budget <= 1000:
        place_to_stay = "Camp"
        price = budget * 0.45
    elif 1000 < budget <= 3000:
        place_to_stay = "Hut"
        price = budget * 0.6
    else:
        place_to_stay = "Hotel"
        price = budget * 0.9
print(f"{locations} - {place_to_stay} - {price:.2f}")