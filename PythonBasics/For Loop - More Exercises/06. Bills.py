months = int(input())
total_electricity = 0

for _ in range(1, months + 1):
    electricity = float(input())

    total_electricity += electricity

water = months * 20
network = months * 15
others = (total_electricity + water + network) * 1.2
avg = (total_electricity + water + network + others) / months

print(f"Electricity: {total_electricity:.2f} lv\nWater: {water:.2f} lv\nInternet: {network:.2f} lv\nOther: {others:.2f} lv\nAverage: {avg:.2f} lv")