n = int(input())

matrix = []

for _ in range(n):
    inner_list = list(input())
    matrix.append(inner_list)

symbol = input()

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            quit()

print(f"{symbol} does not occur in the matrix")