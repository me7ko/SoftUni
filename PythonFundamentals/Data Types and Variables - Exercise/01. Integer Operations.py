num = int(input())
odd = int(num % 2)

while odd == 0:
    input(num)

    if odd != 0:
        break
print(f"{num} is odd!")