products = input().split()
product_to_search = input().split()

stock = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    stock[key] = int(value)

for product in product_to_search:
    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")