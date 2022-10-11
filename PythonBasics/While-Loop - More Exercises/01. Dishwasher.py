counter = 0
plates = 0
pots = 0

init_chemical = int(input()) * 750
chemical = init_chemical

init_input = input()
while init_input != "End":
    dishes = int(init_input)
    counter += 1
    if counter % 3 == 0:
        pots += dishes
        chemical -= 15 * dishes
    else:
        plates += dishes
        chemical -= 5 * dishes
    if chemical < 0:
        break
    init_input = input()
if chemical < 0:
    print(f"Not enough detergent, {abs(chemical)} ml. more necessary!")
else:
    print(f"Detergent was enough!\n{plates} dishes and {pots} pots were washed.\nLeftover detergent {chemical} ml.")