lst = input().split()
k = int(input())

final_numbers = []
position = k - 1
index = 0
len_list = (len(lst))

while len_list > 0:
    index = (position + index) % len_list
    final_numbers.append(lst.pop(index))
    len_list -= 1


print(f"[{','.join(final_numbers)}]")