events = input().split("|")

energy = 100
coins = 100

for command in events:
    split_command = command.split("-")
    event = split_command[0]
    coin = int(split_command[1])
    if event == "rest":
        rest_points = coin
        if energy + rest_points > 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        else:
            energy += rest_points
            print(f"You gained {rest_points} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += coin
            print(f"You earned {coin} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        ingredient = event
        price = coin
        if coins >= price:
            coins -= price
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            exit()

print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")