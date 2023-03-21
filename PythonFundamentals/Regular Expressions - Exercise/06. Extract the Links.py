import re

pattern = r"(www\.[A-Za-z\d\-]+(\.[a-z]+)+)"


while True:
    line = input()
    if not line:
        break

    matches = re.findall(pattern, line)
    if matches:
        match = matches[0]
        print(match[0])

