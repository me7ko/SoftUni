size = int(input())

matrix = [[int(x)for x in input().split()] for _ in range(size)]

data = input().split()
while data[0] != "END":
    command, row, col, value = data[0], int(data[1]), int(data[2]), int(data[3])

    if not (0 <= row < size and 0 <= col < size):
        print("Invalid coordinates")
    elif command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value

    data = input().split()

[print(*el) for el in matrix]
