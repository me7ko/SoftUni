hours_input = int(input())
minutes_input = int(input())


minutes_input += hours_input * 60
minutes_input += 15

hour = int(minutes_input / 60)
minutes = minutes_input % 60

if hour == 24:
    hour = 0
if minutes == 60:
    minutes = 0

if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")

