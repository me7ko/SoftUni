def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(a, b, c):
    first_two_sum = sum_numbers(a, b)
    return subtract(first_two_sum, c)


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))