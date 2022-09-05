import math

record = float(input())
distance = float(input())
time = float(input())

total = distance * time + math.floor((distance / 15)) * 12.5
if record > total:
    print(f"Yes, he succeeded! The new world record is {total:.2f} seconds.")
else:
    print(f"No, he failed! He was {total - record:.2f} seconds slower.")
