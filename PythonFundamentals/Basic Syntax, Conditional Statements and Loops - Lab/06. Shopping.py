total = 0
flag = False
budget = int(input())

price = input()
while price != "End":
    price = int(price)
    total += price
    if total > budget:
        flag = True
        break
    price = input()
if flag:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")