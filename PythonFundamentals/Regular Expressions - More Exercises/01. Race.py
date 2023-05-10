import re

name_pattern = r"[A-Za-z]+"
km_pattern = r"\d"
participants = input().split(", ")

names_by_km = {}

text = input()
while text != "end of race":
    name_matches = re.findall(name_pattern, text)
    name = f"{''.join(name_matches)}"

    km_matches = re.findall(km_pattern, text)
    int_km = [int(km) for km in km_matches]
    sum_km = sum(int_km)
    if name in participants:
        if name not in names_by_km:
            names_by_km[name] = sum_km
        else:
            names_by_km[name] += sum_km

    text = input()

sorted_name_by_km_dict = sorted(names_by_km.items(), key=lambda x: -x[1])
for counter, group in enumerate(sorted_name_by_km_dict, start=1):
    if counter == 1:
        print(f"1st place: {group[0]}")
    if counter == 2:
        print(f"2nd place: {group[0]}")
    if counter == 3:
        print(f"3rd place: {group[0]}")