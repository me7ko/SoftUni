days = int(input())
room = input()
grade = input()
price = 0

if room == "room for one person":
    price = 18 * (days - 1)
elif room == "apartment":
    price = 25 * (days - 1)
    if days < 10:
        price *= 0.7
    elif 10 <= days <= 15:
        price *= 0.65
    else:
        price *= 0.5
elif room == "president apartment":
    price = 35 * (days - 1)
    if days < 10:
        price *= 0.9
    elif 10 <= days <= 15:
        price *= 0.85
    else:
        price *= 0.8
if grade == "positive":
    price *= 1.25
elif grade == "negative":
    price *= 0.9
print(f"{price:.2f}")