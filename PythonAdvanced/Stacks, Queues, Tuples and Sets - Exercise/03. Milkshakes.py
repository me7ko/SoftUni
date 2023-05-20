from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes != 5 and chocolates and cups_of_milk:
    last_chocolate = chocolates.pop()
    first_cup = cups_of_milk.popleft()

    if last_chocolate <= 0 and first_cup <= 0:
        continue
    elif last_chocolate <= 0:
        cups_of_milk.appendleft(first_cup)
        continue
    if first_cup <= 0:
        chocolates.appendleft(last_chocolate)
        continue

    if last_chocolate == first_cup:
        milkshakes += 1
    else:
        cups_of_milk.append(first_cup)
        chocolates.append(last_chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")



