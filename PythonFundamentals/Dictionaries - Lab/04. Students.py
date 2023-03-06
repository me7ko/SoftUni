data = input()

courses = {}
while ":" in data:
    student_name, student_id, course = data.split(":")
    if course not in courses:
        courses[course] = {student_id: student_name}
    else:
        courses[course][student_id] = student_name

    data = input()

replaced_data = data.replace("_", " ")
students = courses[replaced_data]
for student_id, student_name in students.items():
    print(f"{student_name} - {student_id}")