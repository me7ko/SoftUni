info = input()

courses = {}

while info != "end":
    course, student = info.split(" : ")
    if course not in courses:
        courses[course] = [student]
    else:
        courses[course].append(student)

    info = input()

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")