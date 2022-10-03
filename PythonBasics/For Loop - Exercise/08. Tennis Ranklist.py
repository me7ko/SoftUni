tournaments_count = int(input())
init_points = int(input())

final_points = init_points
win = 0
for i in range(1, tournaments_count + 1):
    type_tournament = input()

    if type_tournament == "W":
        final_points += 2000
        win += 1
    elif type_tournament == "F":
        final_points += 1200
    elif type_tournament == "SF":
        final_points += 720

average_points = int((final_points - init_points) / tournaments_count)
win_percentage = win / tournaments_count * 100

print(f"Final points: {final_points}\nAverage points: {average_points}")
print(f"{win_percentage:.2f}%")




