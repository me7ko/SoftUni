resources = {}

while True:
    ore = input()
    if ore == "stop":
        break
    quantity = int(input())
    if ore not in resources:
        resources[ore] = quantity
    else:
        resources[ore] += quantity

for ore, quantity in resources.items():
    print(f"{ore} -> {quantity}")
