season = input()
type_of_group = input()
students_count = int(input())
nights_count = int(input())

price = 0
sport = ""
if season == "Winter":
    if type_of_group in ["boys", "girls"]:
        price = students_count * 9.6 * nights_count
    elif type_of_group == "mixed":
        price = students_count * 10 * nights_count

elif season == "Spring":
    if type_of_group in ["boys", "girls"]:
        price = students_count * 7.2 * nights_count
    elif type_of_group == "mixed":
        price = students_count * 9.5 * nights_count

elif season == "Summer":
    if type_of_group in ["boys", "girls"]:
        price = students_count * 15 * nights_count
    elif type_of_group == "mixed":
        price = students_count * 20 * nights_count

if students_count >= 50:
    price *= 0.5
elif 20 <= students_count < 50:
    price *= 0.85
elif 10 <= students_count < 20:
    price *= 0.95

if season == "Winter":
    if type_of_group == "girls":
        sport = "Gymnastics"
    elif type_of_group == "boys":
        sport = "Judo"
    elif type_of_group == "mixed":
        sport = "Ski"

elif season == "Spring":
    if type_of_group == "girls":
        sport = "Athletics"
    elif type_of_group == "boys":
        sport = "Tennis"
    elif type_of_group == "mixed":
        sport = "Cycling"

elif season == "Summer":
    if type_of_group == "girls":
        sport = "Volleyball"
    elif type_of_group == "boys":
        sport = "Football"
    elif type_of_group == "mixed":
        sport = "Swimming"

print(f"{sport} {price:.2f} lv.")
