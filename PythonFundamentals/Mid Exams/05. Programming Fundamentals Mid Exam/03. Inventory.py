journal = input().split(", ")

commands = input()
while commands != "Craft!":
    split_command = commands.split(" - ")
    command = split_command[0]
    item = split_command[1]
    if command.startswith("Collect"):
        if item not in journal:
            journal.append(item)

    elif command.startswith("Drop"):
        if item in journal:
            journal.remove(item)

    elif command.startswith("Combine Items"):
        split_item = item.split(":")
        if split_item[0] in journal:
            idx = journal.index(split_item[0])
            journal.insert(idx + 1, split_item[1])

    elif command.startswith("Renew"):
        if item in journal:
            idx = journal.index(item)
            item_pop = journal.pop(idx)
            journal.append(item_pop)

    commands = input()

print(', '.join(journal))