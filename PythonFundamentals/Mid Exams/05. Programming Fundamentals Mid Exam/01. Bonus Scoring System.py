from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

lst_of_bonuses = []
lst_of_lectures = []
max_bonus = 0
max_lectures = 0

for _ in range(1, number_of_students + 1):
    attendance = int(input())
    lst_of_lectures.append(attendance)
    if number_of_lectures == 0:
        break
    total_bonus = attendance / number_of_lectures * (5 + additional_bonus)
    lst_of_bonuses.append(total_bonus)
    max_bonus = ceil(max(lst_of_bonuses))
    max_lectures = max(lst_of_lectures)

print(f"Max Bonus: {max_bonus}.\nThe student has attended {max_lectures} lectures.")
