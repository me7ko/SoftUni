rows, cols = [int(x) for x in input().split(", ")]

sum_ = 0

matrix = []

for _ in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    matrix.append(inner_list)
    sum_ += sum(inner_list)

print(sum_)
print(matrix)
