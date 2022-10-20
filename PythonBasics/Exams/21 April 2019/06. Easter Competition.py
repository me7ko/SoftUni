max_points = 0
baker_winner = ""

kozunak_count = int(input())
for times in range(1, kozunak_count + 1):
    baker = input()

    points = 0
    grade = input()
    while True:
        grade = int(grade)
        points += grade

        grade = input()
        if grade == "Stop":
            print(f"{baker} has {points} points.")
            if points > max_points:
                max_points = points
                baker_winner = baker
                print(f"{baker} is the new number 1!")
            break

print(f"{baker_winner} won competition with {max_points} points!")