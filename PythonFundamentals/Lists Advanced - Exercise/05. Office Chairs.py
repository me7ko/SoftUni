rooms = int(input())
flag = True
free_chairs = 0
for room in range(1, rooms + 1):
    chairs = input().split()
    if len(chairs[0]) < int(chairs[1]):
        print(f"{int(chairs[1]) - len(chairs[0])} more chairs needed in room {room}")
        flag = False
    else:
        free_chairs += len(chairs[0]) - int(chairs[1])

if flag:
    print(f"Game On, {free_chairs} free chairs left")