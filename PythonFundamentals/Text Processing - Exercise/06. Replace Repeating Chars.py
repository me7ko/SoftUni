sequence = input()

result = sequence[0]
for letter in sequence:
    if letter not in result[-1]:
        result += letter

print(result)