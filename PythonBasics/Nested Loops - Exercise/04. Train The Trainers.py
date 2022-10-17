counter = 0
all_grades = 0

jury_count = int(input())
presentation_name = input()

while presentation_name != "Finish":

    grade_per_presentation = 0
    for j in range(1, jury_count + 1):
        grade = float(input())

        counter += 1
        grade_per_presentation += grade
        all_grades += grade
    avg_per_presentation = grade_per_presentation / jury_count
    print(f"{presentation_name} - {avg_per_presentation:.2f}.")

    presentation_name = input()
avg_all_presentations = all_grades / counter
print(f"Student's final assessment is {avg_all_presentations:.2f}.")