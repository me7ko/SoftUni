fuel = input()
litres_fuel = float(input())
club_card = input()

if fuel == "Gasoline":
    if club_card == "Yes":
        gasoline = (2.22 - 0.18) * litres_fuel
        if 20 <= litres_fuel <= 25:
            gasoline = gasoline - (gasoline * 0.08)
        elif litres_fuel > 25:
            gasoline = gasoline - (gasoline * 0.1)
        print(f"{gasoline:.2f} lv.")
    elif club_card == "No":
        gasoline = 2.22 * litres_fuel
        if 20 <= litres_fuel <= 25:
            gasoline = gasoline - (gasoline * 0.08)
        elif litres_fuel > 25:
            gasoline = gasoline - (gasoline * 0.1)
        print(f"{gasoline:.2f} lv.")

elif fuel == "Diesel":
    if club_card == "Yes":
        diesel = (2.33 - 0.12) * litres_fuel
        if 20 <= litres_fuel <= 25:
            diesel = diesel - (diesel * 0.08)
        elif litres_fuel > 25:
            diesel = diesel - (diesel * 0.1)
        print(f"{diesel:.2f} lv.")
    elif club_card == "No":
        diesel = 2.33 * litres_fuel
        if 20 <= litres_fuel <= 25:
            diesel = diesel - (diesel * 0.08)
        elif litres_fuel > 25:
            diesel = diesel - (diesel * 0.1)
        print(f"{diesel:.2f} lv.")

elif fuel == "Gas":
    if club_card == "Yes":
        gas = (0.93 - 0.08) * litres_fuel
        if 20 <= litres_fuel <= 25:
            gas = gas - (gas * 0.08)
        elif litres_fuel > 25:
            gas = gas - (gas * 0.1)
        print(f"{gas:.2f} lv.")
    elif club_card == "No":
        gas = 0.93 * litres_fuel
        if 20 <= litres_fuel <= 25:
            gas = gas - (gas * 0.08)
        elif litres_fuel > 25:
            gas = gas - (gas * 0.1)
        print(f"{gas:.2f} lv.")