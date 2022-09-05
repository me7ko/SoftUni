puzzle = 2.60
talking_doll = 3
bear = 4.10
minion = 8.20
truck = 2

price_excursion = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

suma = (puzzle * puzzle_count) + (talking_doll * talking_doll_count) + (bear * bear_count) + (minion * minion_count) + (truck * truck_count)
total_count = puzzle_count + talking_doll_count + bear_count + minion_count + truck_count

if total_count >= 50:
    discount = suma * 0.25
else:
    discount = 0

final_price = suma - discount
rent = final_price * 0.10
win = final_price - rent
final = win - price_excursion
if win >= price_excursion:
    print(f"Yes! {final:.2f} lv left.")
else:
    print(f"Not enough money! {price_excursion - win:.2f} lv needed.")