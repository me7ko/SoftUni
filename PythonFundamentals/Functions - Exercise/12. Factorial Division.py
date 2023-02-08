def get_factorial_division(first_num, second_num):
    first_factorial = 1
    second_factorial = 1
    for f_num in range(1, first_num + 1):
        first_factorial *= f_num
    for s_num in range(1, second_num + 1):
        second_factorial *= s_num
    return first_factorial / second_factorial


first_number = int(input())
second_number = int(input())
res = get_factorial_division(first_number, second_number)
print(f"{res:.2f}")