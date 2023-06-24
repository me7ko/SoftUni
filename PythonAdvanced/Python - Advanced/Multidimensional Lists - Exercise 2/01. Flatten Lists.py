init = input().split("|")


matrix = []
for value in init[::-1]:
    matrix.extend(value.split())

print(*matrix)