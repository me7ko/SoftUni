moves = int(input())
points = 0
invalid_number = 0
num_from_0_to_9 = 0
num_from_10_to_19 = 0
num_from_20_to_29 = 0
num_from_30_to_39 = 0
num_from_40_to_50 = 0
for _ in range(1, moves + 1):
    number = int(input())

    if 0 > number or number > 50:
        invalid_number += 1
        points /= 2
    elif number < 10:
        points += + (number * 0.2)
        num_from_0_to_9 += 1
    elif number < 20:
        points += + (number * 0.3)
        num_from_10_to_19 += 1
    elif number < 30:
        points += + (number * 0.4)
        num_from_20_to_29 += 1
    elif number < 40:
        points += + 50
        num_from_30_to_39 += 1
    elif number <= 50:
        points += + 100
        num_from_40_to_50 += 1

percentage_num_from_0_to_9 = num_from_0_to_9 / moves * 100
percentage_num_from_10_to_19 = num_from_10_to_19 / moves * 100
percentage_num_from_20_to_29 = num_from_20_to_29 / moves * 100
percentage_num_from_30_to_39 = num_from_30_to_39 / moves * 100
percentage_num_from_40_to_50 = num_from_40_to_50 / moves * 100
percentage_invalid_numbers = invalid_number / moves * 100

print(f"{points:.2f}\nFrom 0 to 9: {percentage_num_from_0_to_9:.2f}%\n"
      f"From 10 to 19: {percentage_num_from_10_to_19:.2f}%\nFrom 20 to 29: {percentage_num_from_20_to_29:.2f}%\nFrom 30 to 39: {percentage_num_from_30_to_39:.2f}%\n"
      f"From 40 to 50: {percentage_num_from_40_to_50:.2f}%\nInvalid numbers: {percentage_invalid_numbers:.2f}%")


