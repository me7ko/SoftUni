floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    print()
    for room in range(1, rooms + 1):
        if floor == floors:
            print(f"L{floor}{room - 1}", end=" ")
        elif floor % 2 == 0:
            print(f"O{floor}{room - 1}", end=" ")
        elif floor % 2 != 0:
            print(f"A{floor}{room - 1}", end=" ")