rows, cols = [int(x) for x in input().split(", ")]

matrix = []
sub_matrix = []
max_sum = float('-inf')


for _ in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    matrix.append(inner_list)

for row in range(rows - 1):
    for col in range(cols - 1):
        current_num = matrix[row][col]
        below_current_num = matrix[row+1][col]
        next_num = matrix[row][col+1]
        below_next_num = matrix[row+1][col+1]

        current_sum = current_num + below_current_num + next_num + below_next_num

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_num, next_num], [below_current_num, below_next_num]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)

