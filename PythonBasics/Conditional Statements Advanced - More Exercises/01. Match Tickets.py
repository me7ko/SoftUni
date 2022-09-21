import math

budget = float(input())
category = input()
people_count = int(input())

leva = 0
transport = 0
if category == "VIP":
    leva = 499.99
elif category == "Normal":
    leva += 249.99

if 1 <= people_count <= 4:
    transport = budget * 0.75
elif 5 <= people_count <= 9:
    transport = budget * 0.60
elif 10 <= people_count <= 24:
    transport = budget * 0.50
elif 25 <= people_count <= 49:
    transport = budget * 0.40
else:
    transport = budget * 0.25

result = budget - transport
final_result = abs(result - (leva * people_count))
diff = leva * people_count

if result >= diff:
    print(f"Yes! You have {final_result:.2f} leva left.")
else:
    print(f"Not enough money! You need {final_result:.2f} leva.")
