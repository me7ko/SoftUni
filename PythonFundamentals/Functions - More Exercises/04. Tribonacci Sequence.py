def get_tribonacci_nums(n):
    lst = [1, 0, 0]
    for _ in range(n):
        next_num = sum(lst)
        print(next_num, end=" ")
        lst.append(next_num)
        lst.pop(0)


num = int(input())
get_tribonacci_nums(num)
