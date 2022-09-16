price_per_kg_mackerel = float(input())
price_per_kg_tsatsa = float(input())
kg_palamut = float(input())
kg_safrid = float(input())
kg_mussels = int(input())

price_palamut = price_per_kg_mackerel * 1.60
sum_palamut = kg_palamut * price_palamut
price_safrid = price_per_kg_tsatsa * 1.80
sum_safrid = kg_safrid * price_safrid
sum_mussels = kg_mussels * 7.50

total = sum_palamut + sum_safrid + sum_mussels
print(f"{total:.2f}")

