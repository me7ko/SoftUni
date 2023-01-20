a = 97
n = int(input())

for first in range(a, a + n):
    for second in range(a, a + n):
        for third in range(a, a + n):
            print(f"{chr(first)}{chr(second)}{chr(third)}")