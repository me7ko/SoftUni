actor_name = input()
academy_points = float(input())
persons = int(input())
total_points = academy_points

for i in range(1, persons + 1):
    person = input()
    points = float(input())

    result =(len(person) * points) / 2
    total_points += result
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")