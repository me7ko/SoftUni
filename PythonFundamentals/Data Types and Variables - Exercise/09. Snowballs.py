import sys

number_of_balls = int(input())

highest_value = -sys.maxsize
result = ""

for _ in range(1, number_of_balls + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())

    calculation = (weight / time) ** quality
    if calculation > highest_value:
        highest_value = int(calculation)
        result = f"{weight} : {time} = {highest_value} ({quality})"

print(result)