import math

serial_name = input()
ep_length = int(input())
break_length = int(input())

lunch = break_length / 8
chill = break_length / 4

left_time = break_length - lunch - chill
diff = math.ceil(abs(ep_length - left_time))
if ep_length <= left_time:
    print(f"You have enough time to watch {serial_name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {diff} more minutes.")