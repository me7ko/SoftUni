import math

x = int(input())
y = float(input())
z = int(input())
workers_count = int(input())

total_grape = x * y
wine = (total_grape * 0.4) / 2.5

diff = math.floor(abs(wine - z))
per_worker = diff / workers_count
if wine >= z:
    print(f"Good harvest this year! Total wine: {math.ceil(wine)} liters.\n{diff} liters left -> {math.ceil(per_worker)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.ceil(diff)} liters wine needed.")