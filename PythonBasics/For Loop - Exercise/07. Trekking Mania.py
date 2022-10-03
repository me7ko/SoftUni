group_count = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for groups in range(1, group_count + 1):
    people_in_group = int(input())

    if people_in_group <= 5:
        musala += people_in_group
    elif people_in_group <= 12:
        montblanc += people_in_group
    elif people_in_group <= 25:
        kilimanjaro += people_in_group
    elif people_in_group <= 40:
        k2 += people_in_group
    else:
        everest += people_in_group

total_count = musala + montblanc + kilimanjaro + k2 + everest

percentage_musala = musala / total_count * 100
print(f"{percentage_musala:.2f}%")

percentage_montblanc = montblanc / total_count * 100
print(f"{percentage_montblanc:.2f}%")

percentage_kilimanjaro = kilimanjaro / total_count * 100
print(f"{percentage_kilimanjaro:.2f}%")

percentage_k2 = k2 / total_count * 100
print(f"{percentage_k2:.2f}%")

percentage_everest = everest / total_count * 100
print(f"{percentage_everest:.2f}%")