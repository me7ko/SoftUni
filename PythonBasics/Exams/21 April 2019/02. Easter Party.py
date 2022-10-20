guests_count = int(input())
cover = float(input())
budget = float(input())

if 10 <= guests_count <= 15:
    cover *= 0.85
elif 15 < guests_count <= 20:
    cover *= 0.8
elif guests_count > 20:
    cover *= 0.75

total = (guests_count * cover) + (budget * 0.1)
diff = abs(budget - total)

if total >= budget:
    print(f"No party! {diff:.2f} leva needed.")
else:
    print(f"It is party time! {diff:.2f} leva left.")
