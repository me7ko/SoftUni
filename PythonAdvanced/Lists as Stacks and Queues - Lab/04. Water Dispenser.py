from collections import deque

water_quantity = int(input())
people = deque()

name = input()
while name != "Start":
    people.append(name)
    name = input()

command = input()
while command != "End":
    split_command = command.split()
    if len(split_command) == 1:
        water_to_get = int(split_command[0])
        if water_quantity >= water_to_get:
            water_quantity -= water_to_get
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
    else:
        water_to_refill = int(split_command[1])
        water_quantity += water_to_refill

    command = input()

print(f"{water_quantity} liters left")