countries = input().split(", ")
capitals = input().split(", ")

this_dict = dict(zip(countries, capitals))

for country, capital in this_dict.items():
    print(f"{country} -> {capital}")