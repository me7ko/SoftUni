happiness = [int(num) for num in input().split()]
factor = int(input())

multiplied_lst = list(map(lambda x: int(x) * factor, happiness))
filtered_lst = list(filter(lambda x: x >= sum(happiness) / len(happiness), happiness))

if len(filtered_lst) >= len(happiness) / 2:
    print(f"Score: {len(filtered_lst)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_lst)}/{len(happiness)}. Employees are not happy!")