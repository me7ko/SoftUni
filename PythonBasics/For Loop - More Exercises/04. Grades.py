students_count = int(input())
top_students = 0
between_5_4 = 0
between_4_3 = 0
failed = 0
all_grades = 0

for _ in range(1, students_count + 1):
    grade = float(input())
    all_grades += grade
    if grade < 3:
        failed += 1
    elif 3 <= grade <= 3.99:
        between_4_3 += 1
    elif 4 <= grade <= 4.99:
        between_5_4 += 1
    else:
        top_students += 1

avg = all_grades / students_count
percentage_top_students = top_students / students_count * 100
percentage_between_5_4 = between_5_4 / students_count * 100
percentage_between_4_3 = between_4_3 / students_count * 100
percentage_failed = failed / students_count * 100

print(f"Top students: {percentage_top_students:.2f}%\nBetween 4.00 and 4.99: {percentage_between_5_4:.2f}%\nBetween 3.00 and 3.99: {percentage_between_4_3:.2f}%\nFail: {percentage_failed:.2f}%\nAverage: {avg:.2f}")