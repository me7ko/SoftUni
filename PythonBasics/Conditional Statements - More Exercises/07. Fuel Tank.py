fuel = input()
litres_fuel = float(input())

if fuel == "Diesel":
    if litres_fuel >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")
elif fuel == "Gasoline":
    if litres_fuel >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")
elif fuel == "Gas":
    if litres_fuel >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")
else:
    print("Invalid fuel!")