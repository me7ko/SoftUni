import sys

count = int(input())
max_value = -sys.maxsize
min_value = sys.maxsize

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize

even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for num in range(1, count + 1):
    number = float(input())
    if num % 2 == 0:
        even_sum += number
        if number > even_max:
            even_max = number

        if number < even_min:
            even_min = number

    else:
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number

if even_max == -9223372036854775807:
    even_max = "No"
if even_min == min_value:
    even_min = "No"
if odd_max == -max_value:
    odd_max = "No"
if odd_min == min_value:
    odd_min = "No"

if count == 1:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")

elif count == 0:
    print(f"OddSum=0.00,")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
    print(f"EvenSum=0.00,")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")

else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")