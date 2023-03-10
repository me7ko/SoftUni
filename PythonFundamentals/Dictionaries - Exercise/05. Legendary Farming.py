legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}
materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
junk_items = {}

flag = False

while not flag:
    items = input().lower().split()
    for i in range(0, len(items), 2):
        quantity = int(items[i])
        material = items[i + 1]
        if material not in materials:
            if material not in junk_items:
                junk_items[material] = quantity
            else:
                junk_items[material] += quantity
        else:
            materials[material] += quantity
            if materials[material] >= 250:
                materials[material] -= 250
                flag = True
                print(f"{legendary_items[material]} obtained!")
                break

for material, quantity in materials.items():
    print(f"{material}: {quantity}")

for material, quantity in junk_items.items():
    print(f"{material}: {quantity}")