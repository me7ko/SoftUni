import sys

min_num = sys.maxsize

number = input()

while number != "Stop":
    number = int(number)
    if number < min_num:
        min_num = number
    number = input()
print(min_num)

