chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()
price = 0

total_count = chrysanthemums_count + roses_count + tulips_count

if season in ["Spring", "Summer"]:
    price = (chrysanthemums_count * 2) + (roses_count * 4.10) + (tulips_count * 2.5)
    if holiday == "Y":
        price *= 1.15
elif season in ["Autumn", "Winter"]:
    price = (chrysanthemums_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)
    if holiday == "Y":
        price *= 1.15

if tulips_count > 7 and season == "Spring":
    price *= 0.95
if roses_count >= 10 and season == "Winter":
    price *= 0.9
if total_count > 20:
    price *= 0.8
price_arrangement = price + 2
print(f"{price_arrangement:.2f}")


