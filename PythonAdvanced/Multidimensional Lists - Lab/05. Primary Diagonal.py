n = int(input())

matrix = []
sum_ = 0

for row in range(n):
    inner_list = [int(x) for x in input().split()]
    matrix.append(inner_list)
    sum_ += matrix[row][row]

print(sum_)