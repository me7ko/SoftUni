init_number = int(input())
numbers_sum = 0

while True:
    number = int(input())
    numbers_sum += number

    if numbers_sum >= init_number:
        print(numbers_sum)
        break

