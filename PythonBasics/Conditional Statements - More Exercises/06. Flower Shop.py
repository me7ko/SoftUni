import math

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

sum = (magnolias_count * 3.25) + (hyacinths_count * 4) + (roses_count * 3.50) + (cactus_count * 8)
sum_with_tax = sum - (sum * 0.05)

if sum_with_tax < gift_price:
    diff = math.ceil(abs(gift_price - sum_with_tax))
    print(f"She will have to borrow {diff} leva.")
else:
    diff = math.floor(abs(gift_price - sum_with_tax))
    print(f"She is left with {diff} leva.")
