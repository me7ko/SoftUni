data = input().split("-")

phonebook = {}

while True:
    if len(data) == 1:
        break
    name = data[0]
    number = data[1]
    phonebook[name] = number


    data = input().split("-")

lines = int(data[0])

for line in range(lines):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")