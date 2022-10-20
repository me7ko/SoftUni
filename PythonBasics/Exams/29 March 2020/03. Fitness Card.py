available_sum = float(input())
gender = input()
age = int(input())
sport = input()
sport_price = 0

if gender == "m":
    if sport == "Gym":
        sport_price += 42
    elif sport == "Boxing":
        sport_price += 41
    elif sport == "Yoga":
        sport_price += 45
    elif sport == "Zumba":
        sport_price += 34
    elif sport == "Dances":
        sport_price += 51
    elif sport == "Pilates":
        sport_price += 39

elif gender == "f":
    if sport == "Gym":
        sport_price += 35
    elif sport == "Boxing":
        sport_price += 37
    elif sport == "Yoga":
        sport_price += 42
    elif sport == "Zumba":
        sport_price += 31
    elif sport == "Dances":
        sport_price += 53
    elif sport == "Pilates":
        sport_price += 37

if age <= 19:
    sport_price *= 0.8

if available_sum >= sport_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    diff = abs(available_sum - sport_price)
    print(f"You don't have enough money! You need ${diff:.2f} more.")