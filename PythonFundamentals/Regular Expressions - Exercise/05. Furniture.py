import re

pattern = r">>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)"
result = 0
bought_items = []

while True:
    text = input()
    if text == "Purchase":
        break
    match = re.findall(pattern, text)
    if not match:
        continue

    groups = match[0]

    name = groups[0]
    price = float(groups[1])
    quantity = int(groups[3])

    result += price * quantity
    bought_items.append(name)


print("Bought furniture:")
for item in bought_items:
    print(item)
print(f"Total money spend: {result:.2f}")