flag = False
counter = 0

interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

for a in range(interval_start, interval_end + 1):
    for b in range(interval_start, interval_end + 1):
        counter += 1
        result = a + b
        if result == magic_number:
            print(f"Combination N:{counter} ({a} + {b} = {result})")
            flag = True
        if flag:
            break
    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {magic_number}")