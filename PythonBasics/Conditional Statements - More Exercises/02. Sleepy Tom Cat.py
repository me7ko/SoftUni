init_holidays = int(input())

holidays = init_holidays * 127
working_days = (365 - init_holidays) * 63
total_days = holidays + working_days



difference = abs(30000 - total_days)
hours = difference // 60
minutes = difference % 60

if total_days < 30000:
    print(f"Tom sleeps well\n{hours} hours and {minutes} minutes less for play")
else:
    print(f"Tom will run away\n{hours} hours and {minutes} minutes more for play")
