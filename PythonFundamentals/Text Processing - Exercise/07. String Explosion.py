string = input()

result = []

strength = 0

for i in range(len(string)):
    if string[i] == '>':
        strength += int(string[i + 1])
        result.append(">")
        continue

    if strength > 0:
        strength -= 1
        continue

    result.append(string[i])

final_string = ''.join(result)

print(final_string) 