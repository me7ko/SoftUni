events = input().split("|")
current_energy = 100
coins = 0

for event in events:
    gained_energy = 0
    event_args = event.split("-")

    if event_args[0] == "rest":
        current_energy += int(event_args[1])
        gained_energy += int(event_args[1])
        if current_energy + int(event_args[1]) > 100:
            print(f"You gained {100 - int(event_args[1])} energy.")
            energy = 100
        else:
            current_energy += int(event_args[1])

    elif event_args[0] == "order":
        pass



print(current_energy)