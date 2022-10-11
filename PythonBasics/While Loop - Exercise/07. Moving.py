width = int(input())
length = int(input())
height = int(input())
available_cubic_meters = width * length * height

init_input = input()
while init_input != "Done":
    boxes = int(init_input)
    available_cubic_meters -= boxes
    if available_cubic_meters < 0:
        break
    init_input = input()

if available_cubic_meters >= 0:
    print(f"{available_cubic_meters} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(available_cubic_meters)} Cubic meters more.")