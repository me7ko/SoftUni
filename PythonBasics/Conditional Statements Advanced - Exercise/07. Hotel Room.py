month = input()
overnights_count = int(input())
studio = 0
apartment = 0

if month in ["May", "October"]:
    studio = 50 * overnights_count
    apartment = 65 * overnights_count
    if overnights_count > 14:
        studio *= 0.7
        apartment *= 0.9
    elif overnights_count > 7:
        studio *= 0.95


elif month in ["June", "September"]:
    studio = 75.2 * overnights_count
    apartment = 68.7 * overnights_count
    if overnights_count > 14:
        studio *= 0.8
        apartment *= 0.9

elif month in ["July", "August"]:
    studio = 76 * overnights_count
    apartment = 77 * overnights_count
    if overnights_count > 14:
        apartment *= 0.9

print(f"Apartment: {apartment:.2f} lv.\nStudio: {studio:.2f} lv.")