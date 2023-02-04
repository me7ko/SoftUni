items_with_price = input().split("|")
budget = float(input())
init_budget = budget
total_price = []
sum_price = 0
for item in items_with_price:
    item_args = item.split("->")
    item_price = float(item_args[1])

    if item_args[0] == "Clothes" and item_price > 50:
        continue
    if item_args[0] == "Shoes" and item_price > 35:
        continue
    if item_args[0] == "Accessories" and item_price > 20.50:
        continue

    if budget >= item_price:
        budget -= item_price
        total_price.append(round(item_price * 1.4, 2))
        sum_price += round(item_price * 1.4, 2)
profit = (sum_price + budget) - init_budget

for price in total_price:
    print(f"{price:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
if sum_price + budget > 150:
    print("Hello, France!")
else:
    print("Not enough money.")