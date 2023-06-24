set_of_elements = set()

for _ in range(int(input())):
    for el in input().split():
        set_of_elements.add(el)

print(*set_of_elements, sep="\n")