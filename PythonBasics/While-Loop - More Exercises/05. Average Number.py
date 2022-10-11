total = 0
n = int(input())

for num in range(1, n + 1):
    while True:
        number = int(input())
        total += number
        if num == n:
            break
        break
print(f"{total / n:.2f}")