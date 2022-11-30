loafs = 0
colored_eggs = 0
budget = float(input())
price_per_kg_flour = float(input())

price_for_eggs = price_per_kg_flour * 0.75
price_for_milk = (price_per_kg_flour * 1.25) / 4
total = (price_for_eggs + price_per_kg_flour + price_for_milk)
while budget > total:
    budget -= total
    loafs += 1
    colored_eggs += 3
    if loafs % 3 == 0:
        colored_eggs -= loafs - 2
print(f"You made {loafs} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")