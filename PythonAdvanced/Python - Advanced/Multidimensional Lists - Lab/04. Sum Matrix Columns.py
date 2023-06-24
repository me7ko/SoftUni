rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_list = [int(x) for x in input().split()]
    matrix.append(inner_list)

for col in range(cols):
    sum_ = 0

    for row in range(rows):
        current_num = matrix[row][col]
        sum_ += current_num
        
    print(sum_)