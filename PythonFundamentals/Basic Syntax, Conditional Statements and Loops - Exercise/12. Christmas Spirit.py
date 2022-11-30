total_cost = 0
points = 0
days_count = 0
quantity = int(input())
days = int(input())

for _ in range(days, 0, -1):
    days_count += 1

    if days_count % 11 == 0:
        quantity += 2
    if days_count % 2 == 0:
        total_cost += 2 * quantity
        points += 5
    if days_count % 3 == 0:
        total_cost += (5 * quantity) + (3 * quantity)
        points += 13
    if days_count % 5 == 0:
        total_cost += 15 * quantity
        points += 17
        if days_count % 3 == 0:
            points += 30
    if days_count % 10 == 0:
        points -= 20
        total_cost += 23

if days_count % 10 == 0:
    points -= 30

print(f"Total cost: {total_cost}\nTotal spirit: {points}")