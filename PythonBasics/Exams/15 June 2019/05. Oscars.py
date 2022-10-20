actor_name = input()
academy_points = float(input())
judges_count = int(input())

for j in range(1, judges_count + 1):
    judge_name = input()
    judge_points = float(input())
    total_judge = (len(judge_name) * judge_points) / 2
    academy_points += total_judge

    if academy_points > 1250.5:
        break

if academy_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    diff = 1250.5 - academy_points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")