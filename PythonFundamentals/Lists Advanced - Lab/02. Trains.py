num_of_wagons = int(input())

lst_of_wagons = [0] * num_of_wagons

command = input()
while command != "End":
    split_command = command.split()
    if command.startswith("add"):
        lst_of_wagons[-1] += int(split_command[1])
    elif command.startswith("insert"):
        lst_of_wagons[int(split_command[1])] += int(split_command[2])
    elif command.startswith("leave"):
        lst_of_wagons[int(split_command[1])] -= int(split_command[2])

    command = input()

print(lst_of_wagons)