square_meters = float(input())
price_per_meter = 7.61

total_meters = square_meters * price_per_meter
discount = total_meters * 0.18

print(f"The final price is: {total_meters-discount} lv.\nThe discount is: {discount} lv.")
