total = 0
orders = int(input())

for _ in range(1, orders + 1):
    current = 0
    price_per_cap = float(input())
    days = int(input())
    caps_per_day = int(input())

    current += (price_per_cap * caps_per_day) * days

    if (0.01 <= price_per_cap <= 100.00) and (1 <= days <= 31) and (1 <= caps_per_day <= 2000):
        print(f"The price for the coffee is: ${current:.2f}")
        total += current

print(f"Total: ${total:.2f}")
