def check_numbers(first, second, third):
    if (third > 0 > first and second < 0) or (second > 0 > first and third < 0) or \
            (first > 0 > second and third < 0) or (first > 0 and second > 0 and third > 0):
        print("positive")

    elif first == 0 or second == 0 or third == 0:
        print("zero")

    elif first < 0 or second < 0 or third < 0:
        print("negative")


first_num = int(input())
second_num = int(input())
third_num = int(input())

check_numbers(first_num, second_num, third_num)