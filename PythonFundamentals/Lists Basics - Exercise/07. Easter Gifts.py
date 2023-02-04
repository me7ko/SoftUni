gifts_names = input().split()

command = input()

while command != "No Money":
    split_command = command.split()
    if split_command[0] == "OutOfStock":
        for i in range(len(gifts_names)):
            if gifts_names[i] == split_command[1]:
                gifts_names[i] = "None"

    elif split_command[0] == "Required":
        index = int(split_command[2])
        if index > len(gifts_names) or index < 0:
            command = input()
            continue
        gifts_names[index] = split_command[1]

    elif split_command[0] == "JustInCase":
        gifts_names[-1] = split_command[1]

    command = input()

for _ in range(len(gifts_names)):
    if "None" in gifts_names:
        gifts_names.remove("None")

print(*gifts_names)