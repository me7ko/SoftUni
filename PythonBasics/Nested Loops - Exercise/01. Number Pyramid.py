counter = 0
flag = False

n = int(input())

for row in range(1, n + 1):
    print()
    for column in range(1, row + 1):
        counter += 1
        if counter > n:
            flag = True
            break
        print(counter, end=" ")

    if flag:
        break