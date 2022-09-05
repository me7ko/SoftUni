import math

serial_name = input()
ep_length = int(input())
break_length = int(input())
lunch_time = break_length / 8
break_time = break_length / 4

free_time = break_length - (lunch_time + break_time)

if free_time >= ep_length:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(free_time - ep_length)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(ep_length - free_time)} more minutes.")