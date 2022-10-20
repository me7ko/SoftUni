tournament_days = int(input())

day_win = 0
day_lose = 0
total_money = 0
for days in range(1, tournament_days + 1):
    sport = input()
    win_count = 0
    lose_count = 0
    current_money = 0

    while sport != "Finish":

        result = input()
        if result == "win":
            current_money += 20
            win_count += 1
        elif result == "lose":
            lose_count += 1
        sport = input()
    if win_count > lose_count:
        current_money *= 1.1
        day_win += 1
    else:
        day_lose += 1
    total_money += current_money

if day_win > day_lose:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
