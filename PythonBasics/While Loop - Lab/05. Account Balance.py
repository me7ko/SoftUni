total = 0

money = input()
while money != "NoMoreMoney":
    money = float(money)
    if money < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {money:.2f}")
    total += float(money)
    money = input()

print(f"Total: {total:.2f}")

