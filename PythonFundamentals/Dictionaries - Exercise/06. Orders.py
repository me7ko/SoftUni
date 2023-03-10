info = input()

order = {}

while info != "buy":
    product, price, quantity = info.split()
    if product not in order:
        order[product] = [float(price), int(quantity)]
    else:
        order[product][0] = float(price)
        order[product][1] += int(quantity)

    info = input()

for product, info in order.items():
    price = info[0]
    quantity = info[1]
    print(f"{product} -> {price * quantity:.2f}")