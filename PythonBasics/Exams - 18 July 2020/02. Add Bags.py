baggage_price_above_20 = float(input())
baggage_kg = float(input())
days_to_travel = int(input())
baggage_count = int(input())
price = baggage_price_above_20

if baggage_kg < 10:
    price *= 0.2
elif 10 <= baggage_kg <= 20:
    price /= 2
else:
    price = baggage_price_above_20

if days_to_travel < 7:
    price *= 1.4
elif 7 <= days_to_travel <= 30:
    price *= 1.15
else:
    price *= 1.1

total_sum = price * baggage_count
print(f"The total price of bags is: {total_sum:.2f} lv.")