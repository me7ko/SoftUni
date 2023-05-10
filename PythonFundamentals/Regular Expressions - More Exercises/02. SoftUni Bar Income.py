import re

pattern = r"%([A-Z][a-z]+)%[^|$%.]*<(\w+)>[^|$%.]*\|(\d+)\|[^|$%.\d]*(\d+\.?\d*)\$"

total_income = 0

text = input()
while text != "end of shift":

    matches = re.findall(pattern, text)
    if matches:
        group = matches[0]
        name = group[0]
        product = group[1]
        quantity = int(group[2])
        price = float(group[3])
        total_income += quantity * price
        print(f"{name}: {product} - {quantity * price:.2f}")

    text = input()

print(f"Total income: {total_income:.2f}")