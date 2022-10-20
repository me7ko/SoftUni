film_budget = float(input())
destination = input()
season = input()
days_count = int(input())

money = 0

if season == "Winter":
    if destination == "Dubai":
        money += 45000
    elif destination == "Sofia":
        money += 17000
    elif destination == "London":
        money += 24000

elif season == "Summer":
    if destination == "Dubai":
        money += 40000
    elif destination == "Sofia":
        money += 12500
    elif destination == "London":
        money += 20250

final_money = money * days_count

if destination == "Dubai":
    final_money *= 0.7
elif destination == "Sofia":
    final_money *= 1.25

diff = abs(film_budget - final_money)
if film_budget >= final_money:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")