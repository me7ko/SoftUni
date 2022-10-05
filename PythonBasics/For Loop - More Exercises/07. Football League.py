capacity = int(input())
fans_count = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for _ in range(1, fans_count + 1):
    sector = input()

    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

percentage_sector_a = sector_a / fans_count * 100
percentage_sector_b = sector_b / fans_count * 100
percentage_sector_v = sector_v / fans_count * 100
percentage_sector_g = sector_g / fans_count * 100
percentage_fans_capacity = fans_count / capacity * 100

print(f"{percentage_sector_a:.2f}%\n{percentage_sector_b:.2f}%\n{percentage_sector_v:.2f}%\n"
      f"{percentage_sector_g:.2f}%\n{percentage_fans_capacity:.2f}%")