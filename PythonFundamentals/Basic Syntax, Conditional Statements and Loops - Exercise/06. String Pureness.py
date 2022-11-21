number = int(input())

for _ in range(1, number + 1):
    str = input()
    if "," in str or "." in str or "_" in str:
        print(f"{str} is not pure!")
    else:
        print(f"{str} is pure.")