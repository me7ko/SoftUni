num_of_commands = int(input())

parking = {}

for num in range(num_of_commands):
    commands = input().split()
    if commands[0] == "register":
        username = commands[1]
        plate = commands[2]
        if username not in parking:
            parking[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    else:
        username = commands[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            parking.pop(username)
            print(f"{username} unregistered successfully")

for username, plate in parking.items():
    print(f"{username} => {plate}")

