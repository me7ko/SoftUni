command = ""
init_input = input()

lst = init_input.split(", ")
wolf_place = len(lst) - 1

for animal in lst:
    if animal == "wolf" and wolf_place == 0:
        command = "Please go away and stop eating my sheep"
    elif animal == "wolf":
        command = f"Oi! Sheep number {wolf_place}! You are about to be eaten by a wolf!"
    wolf_place -= 1

print(command)