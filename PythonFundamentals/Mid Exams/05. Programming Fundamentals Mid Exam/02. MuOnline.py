rooms = input().split("|")
health = 100
bitcoins = 0
room_count = 0
flag = True
for room in rooms:
    split_room = room.split()
    command = split_room[0]
    number = int(split_room[1])
    room_count += 1
    if command == "potion":
        if health + number > 100:
            number = 100 - health
        health += number
        print(f"You healed for {number} hp.\nCurrent health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.\nBest room: {room_count}")
            flag = False
            break
if flag:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")


