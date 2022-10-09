name = input()

all_grades = 0
year = 0
fails = 0

while True:
    grade = float(input())

    year += 1

    if grade < 4:

        fails += 1
        if fails == 2:
            print(f"{name} has been excluded at {year} grade")
            break
        year -= 1

    else:
        all_grades += grade

    if year == 12:
        avg = all_grades / 12
        print(f"{name} graduated. Average grade: {avg:.2f}")
        break