pair_of_rows = int(input())

students_info = {}

for row in range(pair_of_rows):
    student = input()
    grade = float(input())

    if student not in students_info:
        students_info[student] = [grade]
    else:
        students_info[student].append(grade)

for student, grades in students_info.items():
    if sum(grades) / len(grades) >= 4.5:
        print(f"{student} -> {sum(grades) / len(grades):.2f}")