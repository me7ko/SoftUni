a1 = int(input())
a2 = int(input())
n = int(input())


for symb1 in range(a1, a2):
    char = chr(symb1)
    for symb2 in range(1, n):
        for symb3 in range(1, n // 2):
            if symb1 % 2 != 0 and (symb1 + symb2 + symb3) % 2 != 0:
                print(f"{char}-{symb2}{symb3}{symb1}")