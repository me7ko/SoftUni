pens = 5.80
markers = 7.20
preparat = 1.20

number_of_pens = int(input())
numbers_of_markers = int(input())
litres_of_preparat= int(input())
procent_discount = int(input())/100

price_pens = pens * number_of_pens
price_markers = markers * numbers_of_markers
price_preparat = preparat * litres_of_preparat

total = price_pens + price_markers + price_preparat

total_with_discount = total - (total * procent_discount)

print(total_with_discount)

