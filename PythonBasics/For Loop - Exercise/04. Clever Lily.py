age = int(input())
machine_price = float(input())
toy_price = int(input())

toys = 0
money = 0
total_money = 0

for birthday in range(1, age + 1):
    if birthday % 2 != 0:
        toys += 1
    else:
        money += 10
        total_money += money - 1
total_toys = toys * toy_price
all_total = total_money + total_toys

diff = abs(all_total - machine_price)
if all_total >= machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")