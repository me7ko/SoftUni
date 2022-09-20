init_hours = int(input())
init_minutes = int(input())

all_time = (init_hours * 60) + init_minutes + 15

hours = all_time // 60
minutes = all_time % 60

if hours == 24:
    hours = 0

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
