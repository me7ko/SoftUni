happy_year = int(input())
condition = False

while not condition:
    happy_year += 1
    set_year = set()
    for i in range(len(str(happy_year))):
        set_year.add(str(happy_year)[i])

    condition = len(set_year) == len(str(happy_year))

print(happy_year)