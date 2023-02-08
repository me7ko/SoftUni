inp = [int(x) for x in input().split(", ")]

for idx in range(len(inp)):
    num = inp[idx]
    if num == 0:
        popped = inp.pop(idx)
        inp.append(popped)
        for idx_2 in range(len(inp)):
            num = inp[idx_2]
            if num == 0:
                popped = inp.pop(idx_2)
                inp.append(popped)

print(inp)