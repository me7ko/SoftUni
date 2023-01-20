helmet_count = 0
sword_count = 0
shield_count = 0
armor_count = 0

lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

for lost in range(1, lost_fights + 1):
    if lost % 2 == 0:
        helmet_count += 1
    if lost % 3 == 0:
        sword_count += 1
    if lost % 6 == 0:
        shield_count += 1
    if lost % 12 == 0:
        armor_count += 1

final_price = helmet_price * helmet_count + sword_price * sword_count + shield_price * shield_count + armor_price * armor_count
print(f"Gladiator expenses: {final_price:.2f} aureus")

