price_excursion = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_price = (puzzle_count * 2.6) + (dolls_count * 3) + (bears_count * 4.1) + (minions_count * 8.2) + (trucks_count * 2)
total_toys = puzzle_count + dolls_count + bears_count + minions_count + trucks_count

if total_toys >= 50:
    total_price = total_price - (total_price * 0.25)

total_price = total_price - (total_price * 0.1)

diff = abs(price_excursion - total_price)
if price_excursion <= total_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")