import math

serial_name = input()
seasons_count = int(input())
episodes_count = int(input())
time = float(input())

ads = time * 0.2
total_length = ads + time
special_episodes = seasons_count * 10
total_time = total_length * episodes_count * seasons_count + special_episodes
print(f"Total time needed to watch the {serial_name} series is {math.floor(total_time)} minutes.")

