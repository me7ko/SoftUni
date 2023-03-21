import re

pattern = r"\d+"
lst_of_matches = []
while True:
    text = input()
    if not text:
        break
    matches = re.findall(pattern, text)
    lst_of_matches.extend(matches)

print(*lst_of_matches)