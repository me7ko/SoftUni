n = int(input())

for num in range(1, n + 1):
    first_num = num // 10
    second_num = num % 10
    if first_num + second_num == 5 or first_num + second_num == 7 or first_num + second_num == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")