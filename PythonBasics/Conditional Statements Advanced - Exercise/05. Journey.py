budget = float(input())
season = input()

visit_place = ""
sleep_place = ""


if budget <= 100:
    visit_place = "Bulgaria"
    if season == "summer":
        sleep_place = "Camp"
        budget *= 0.3
    elif season == "winter":
        sleep_place = "Hotel"
        budget *= 0.7

elif budget <= 1000:
    visit_place = "Balkans"
    if season == "summer":
        sleep_place = "Camp"
        budget *= 0.4
    elif season == "winter":
        sleep_place = "Hotel"
        budget *= 0.8

else:
    visit_place = "Europe"
    sleep_place = "Hotel"
    budget *= 0.9

print(f"Somewhere in {visit_place}\n{sleep_place} - {budget:.2f}")