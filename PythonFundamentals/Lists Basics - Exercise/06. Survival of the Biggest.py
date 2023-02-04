nums = input().split()
num_count_to_remove = int(input())

int_nums_lst = []

for idx in range(len(nums)):
    current_num = int(nums[idx])
    int_nums_lst.append(current_num)

for _ in range(num_count_to_remove):
    int_nums_lst.remove(min(int_nums_lst))

print(*int_nums_lst, sep=", ")
