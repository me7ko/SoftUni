current_money = 0
destination = input()

while destination != "End":
    min_budget = float(input())
    money = float(input())

    while current_money < min_budget:
        current_money += money

        if current_money >= min_budget:
            print(f"Going to {destination}!")
            current_money = 0
            break

        money = float(input())

    destination = input()