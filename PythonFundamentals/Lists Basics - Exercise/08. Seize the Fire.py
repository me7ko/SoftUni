fires_with_cells = input().split("#")
water = int(input())

cells = []
total_fire = 0
for cell in fires_with_cells:
    cell_args = cell.split(" = ")
    fire_type = cell_args[0]
    range_of_fire = int(cell_args[1])

    if fire_type == "High" and (range_of_fire < 81 or range_of_fire > 125):
        continue
    if fire_type == "Medium" and (range_of_fire < 51 or range_of_fire > 80):
        continue
    if fire_type == "Low" and (range_of_fire < 1 or range_of_fire > 50):
        continue

    if range_of_fire > water:
        continue

    water -= range_of_fire
    total_fire += range_of_fire
    cells.append(range_of_fire)

print("Cells:")
for cell in cells:
    print(f" - {cell}")
effort = total_fire * 0.25
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")