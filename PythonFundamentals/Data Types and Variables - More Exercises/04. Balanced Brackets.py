check = 0

lines = int(input())

for _ in range(1, lines + 1):
    idx = input()
    if idx == "(":
        check += 1
    elif idx == ")":
        check -= 1
    if check != 0 and check != 1:
        print("UNBALANCED")
        break
else:
    print("BALANCED")