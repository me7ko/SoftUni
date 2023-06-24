students = {}

for _ in range(int(input())):
    name, grade = tuple(input().split())
    grade = float(grade)

    if name not in students:
        students[name] = []
    students[name].append(grade)

for key, value in students.items():
    avg = sum(value) / len(value)
    print(f"{key} -> {' '.join([str(f'{x:.2f}') for x in value])} (avg: {avg:.2f})")