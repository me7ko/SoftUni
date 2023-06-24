from collections import deque

clothes = deque(int(x) for x in input().split())

rack_capacity = int(input())

current_rack = rack_capacity
num_of_racks = 1

while clothes:
    cloth = clothes.pop()

    if current_rack >= cloth:
        current_rack -= cloth
    else:
        num_of_racks += 1
        current_rack = rack_capacity - cloth

print(num_of_racks)




