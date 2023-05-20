rows = int(input())

flatten_matrix = []

for _ in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    flatten_matrix.extend(inner_list)

print(flatten_matrix)