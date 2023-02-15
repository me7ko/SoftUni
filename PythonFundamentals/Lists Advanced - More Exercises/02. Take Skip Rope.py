main_string = input()

numbers = []
letters = []
output = []
[numbers.append(int(x)) if x.isdigit() else letters.append(x) for x in main_string]

while numbers:
    take = numbers.pop(0)
    skip = numbers.pop(0)
    output += letters[:take]
    letters = letters[take + skip:]

print(*output, sep="")