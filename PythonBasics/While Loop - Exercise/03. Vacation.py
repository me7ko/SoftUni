spending_days = 0
total_days = 0
flag = False
money_needed = float(input())
available_money = float(input())

while available_money < money_needed:
    command = input()
    money = float(input())
    total_days += 1
    if command == "spend":
        available_money -= money
        spending_days += 1
        if available_money < 0:
            available_money = 0
    elif command == "save":
        available_money += money
        spending_days = 0
    if spending_days == 5:
        flag = True
        break

if flag:
    print(f"You can't save the money.\n{total_days}")
else:
    print(f"You saved the money for {total_days} days.")
