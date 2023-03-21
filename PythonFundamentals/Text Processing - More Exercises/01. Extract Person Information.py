import re

name_pattern = r"@([A-Za-z]+)\|"
age_pattern = r"#([\d]+)\*"

lines = int(input())

for _ in range(lines):
    text = input()

    name_matches = re.findall(name_pattern, text)
    age_matches = re.findall(age_pattern, text)

    print(f"{name_matches[0]} is {age_matches[0]} years old.")