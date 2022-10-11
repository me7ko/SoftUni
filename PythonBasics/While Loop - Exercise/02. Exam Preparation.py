all_grades = 0
failed = 0
problems_count = 0
flag = False

poor_grades = int(input())

problem_name = input()
while problem_name != "Enough":
    grade = int(input())
    all_grades += grade
    problems_count += 1
    last_problem = problem_name
    if grade <= 4:
        failed += 1
        if failed == poor_grades:
            flag = True
            break
    problem_name = input()
avg = all_grades / problems_count

if flag:
    print(f"You need a break, {poor_grades} poor grades.")
else:
    print(f"Average score: {avg:.2f}\nNumber of problems: {problems_count}\nLast problem: {last_problem}")