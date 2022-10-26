import math

days = int(input())
ran_km = float(input())
total_days = ran_km
total = ran_km
for _ in range(1, days + 1):
    percentage = int(input())
    total_days *= (1 + percentage / 100)
    total += total_days

diff = abs(total - 1000)
if total < 1000:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(diff)} more kilometers")
else:
    print(f"You've done a great job running {math.ceil(diff)} more kilometers!")


