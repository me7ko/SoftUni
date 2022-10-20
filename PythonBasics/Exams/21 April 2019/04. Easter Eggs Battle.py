flag = False
first_count = int(input())
second_count = int(input())


winner = input()
while winner != "End":
    if winner == "one":
        second_count -= 1
    elif winner == "two":
        first_count -= 1

    if first_count == 0:
        print(f"Player one is out of eggs. Player two has {second_count} eggs left.")
        flag = True
        break
    elif second_count == 0:
        print(f"Player two is out of eggs. Player one has {first_count} eggs left.")
        flag = True
        break

    winner = input()

if not flag:
    print(f"Player one has {first_count} eggs left.\nPlayer two has {second_count} eggs left.")

