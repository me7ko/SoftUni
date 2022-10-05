loads_count = int(input())
total_loads = 0
average = 0
van = 0
truck = 0
train = 0

for _ in range(1, loads_count + 1):
    tons_per_load = int(input())
    total_loads += tons_per_load
    if tons_per_load <= 3:
        van += tons_per_load
    elif 4 <= tons_per_load <= 11:
        truck += tons_per_load
    else:
        train += tons_per_load

avg = ((van * 200) + (truck * 175) + (train * 120)) / total_loads
percentage_van = van / total_loads * 100
percentage_truck = truck / total_loads * 100
percentage_train = train / total_loads * 100

print(f"{avg:.2f}\n{percentage_van:.2f}%\n{percentage_truck:.2f}%\n{percentage_train:.2f}%")
