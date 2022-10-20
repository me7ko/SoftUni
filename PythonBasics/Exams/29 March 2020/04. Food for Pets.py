total_dog = 0
total_cat = 0
all_total = 0
cookies = 0

days_count = int(input())
total_food = float(input())

for days in range(1, days_count + 1):
    dog_count = int(input())
    cat_count = int(input())

    total_dog += dog_count
    total_cat += cat_count

    if days % 3 == 0:
        cookies += (dog_count + cat_count) * 0.1

all_total = total_dog + total_cat
percentage_eaten = (all_total / total_food) * 100
percentage_dog = total_dog / all_total * 100
percentage_cat = total_cat / all_total * 100

print(f"Total eaten biscuits: {int(cookies)}gr.\n{percentage_eaten:.2f}% of the food has been eaten.\n{percentage_dog:.2f}% eaten from the dog.\n{percentage_cat:.2f}% eaten from the cat.")