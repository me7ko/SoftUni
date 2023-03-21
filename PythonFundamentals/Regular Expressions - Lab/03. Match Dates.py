import re

pattern = r"\b(?P<Day>\d{2})([-./])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"
text = input()

matches = re.findall(pattern, text)

for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")