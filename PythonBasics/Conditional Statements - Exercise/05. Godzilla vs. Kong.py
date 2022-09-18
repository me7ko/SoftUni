budget = float(input())
statistics_count = int(input())
cloth_price = float(input())

sum_decor = budget * 0.10
sum_cloth = statistics_count * cloth_price

if statistics_count > 150:
    discount = sum_cloth * 0.10
else:
    discount = 0

total_sum = sum_decor + sum_cloth - discount
budget_left = budget - total_sum


if total_sum > budget:
    print(f"Not enough money!\nWingard needs {total_sum-budget:.2f} leva more.")
elif total_sum <= budget:
    print(f"Action!\nWingard starts filming with {budget - total_sum:.2f} leva left.")