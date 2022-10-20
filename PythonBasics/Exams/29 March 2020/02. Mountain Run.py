import math

record_in_seconds = float(input())
record_in_meters = float(input())
time_in_seconds = float(input())

total = record_in_meters * time_in_seconds
delay = math.floor(record_in_meters / 50) * 30

total_time = total + delay

if total_time >= record_in_seconds:
    diff = abs(total_time - record_in_seconds)
    print(f"No! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")