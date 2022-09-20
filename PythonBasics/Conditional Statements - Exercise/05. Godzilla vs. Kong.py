budget_of_film = float(input())
statists_count = int(input())
price_per_cloth = float(input())

all_price = statists_count * price_per_cloth
decor = budget_of_film * 0.1

if statists_count > 150:
    all_price = all_price - (all_price * 0.1)
total_price = all_price + decor

diff = abs(budget_of_film - total_price)
if budget_of_film < total_price:
    print(f"Not enough money!\nWingard needs {diff:.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {diff:.2f} leva left.")
