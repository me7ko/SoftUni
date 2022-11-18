import sys

max_num = -sys.maxsize

first_num = int(input())
second_num = int(input())

for n in range(1, second_num + 1):
    if n % first_num == 0:
        if n > max_num:
            max_num = n
print(max_num)
