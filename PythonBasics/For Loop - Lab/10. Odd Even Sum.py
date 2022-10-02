n_count_numbers = int(input())
even = 0
odd = 0

for num in range(n_count_numbers):
    number = int(input())
    if num % 2 == 0:
        even += number
    else:
        odd += number

if even == odd:
    print(f"Yes\nSum = {even}")
else:
    diff = abs(even-odd)
    print(f"No\nDiff = {diff}")

