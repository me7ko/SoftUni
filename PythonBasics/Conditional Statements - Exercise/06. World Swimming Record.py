import math

record_in_seconds = float(input())
distance_meters = float(input())
time_seconds = float(input())

distance_traveled = distance_meters * time_seconds
delay = math.floor(distance_meters / 15) * 12.5
total_time = distance_traveled + delay


if record_in_seconds <= total_time:
    diff = total_time - record_in_seconds
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")