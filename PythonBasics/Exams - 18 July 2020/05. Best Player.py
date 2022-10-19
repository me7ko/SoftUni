highest_count_goals = 0
best_player = ""
flag = False
player_name = input()
while player_name != "END":
    goals_count = int(input())

    if goals_count > highest_count_goals:
        highest_count_goals = goals_count
        best_player = player_name
    if goals_count >= 3:
        flag = True
    if goals_count >= 10:
        break
    player_name = input()

if flag:
    print(f"{best_player} is the best player!\nHe has scored {highest_count_goals} goals and made a hat-trick !!!")
else:
    print(f"{best_player} is the best player!\nHe has scored {highest_count_goals} goals.")