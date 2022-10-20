kozunak_count = int(input())
eggs_count = int(input())
kg_cookie = int(input())

kozunak_price = kozunak_count * 3.2
eggs_price = eggs_count * 4.35
cookies_price = kg_cookie * 5.4
egg_paint = eggs_count * 12 * 0.15

total = kozunak_price + eggs_price + cookies_price + egg_paint
print(f"{total:.2f}")