def price_function(product, quantity):
    final_price = 0
    if product == "coffee":
        final_price += 1.5 * quantity
    elif product == "water":
        final_price += 1 * quantity
    elif product == "coke":
        final_price += 1.4 * quantity
    elif product == "snacks":
        final_price += 2 * quantity
    return final_price


product = input()
quantity = int(input())

result = price_function(product, quantity)
print(f"{result:.2f}")