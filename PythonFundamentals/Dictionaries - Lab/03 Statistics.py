commands = input()

products = {}

while commands != "statistics":
    command = commands.split(": ")
    key = command[0]
    value = int(command[1])
    if key not in products:
        products[key] = value
    else:
        products[key] += value

    commands = input()

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}\nTotal Quantity: {sum(products.values())}")