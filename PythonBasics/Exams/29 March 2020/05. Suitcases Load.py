counter = 0
flag = True
suitcases = 0

trunk_space = float(input())
suitcase_volume = input()

while suitcase_volume != "End":
    suitcase_volume = float(suitcase_volume)
    counter += 1

    if counter % 3 == 0:
        suitcase_volume *= 1.1

    if trunk_space - suitcase_volume < 0:
        print("No more space!")
        flag = False
        break

    trunk_space -= suitcase_volume

    suitcases += 1
    suitcase_volume = input()

if flag:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcases} suitcases loaded.")