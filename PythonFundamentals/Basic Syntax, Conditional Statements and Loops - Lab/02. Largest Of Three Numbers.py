import sys

max_num = -sys.maxsize

first_num = float(input())
second_num = float(input())
third_num = float(input())

if first_num > max_num:
    max_num = first_num
if second_num > max_num:
    max_num = second_num
if third_num > max_num:
    max_num = third_num

print(int(max_num))