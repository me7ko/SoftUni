import sys

user_input = int(input())
max_number = -sys.maxsize
first_sum = 0

for num in range(1, user_input + 1):
    number = int(input())
    if number > max_number:
        max_number = number
    first_sum += number
total_sum = first_sum - max_number
if total_sum == max_number:
    print(f"Yes\nSum = {total_sum}")
else:
    diff = abs(total_sum - max_number)
    print(f"No\nDiff = {diff}")