CAPACITY = 255
tank = 0

n = int(input())
for _ in range(n):
    liters = int(input())
    if tank + liters > CAPACITY:
        print("Insufficient capacity!")
    else:
        tank += liters

print(tank)