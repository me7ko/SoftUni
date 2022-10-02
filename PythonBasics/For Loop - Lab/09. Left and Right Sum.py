n_count_numbers = int(input())
left_sum = 0
right_sum = 0

for num in range(n_count_numbers * 2):
    number = int(input())
    if num < n_count_numbers:
        left_sum += number
    elif num >= n_count_numbers:
        right_sum += number

if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    diff = abs(left_sum-right_sum)
    print(f"No, diff = {diff}")

