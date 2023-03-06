words = input().lower().split()

odd_occurrences = {}
default_value = 1

for word in words:
    if word not in odd_occurrences:
        odd_occurrences[word] = default_value
    else:
        odd_occurrences[word] += 1

for key, value in odd_occurrences.items():
    if value % 2 != 0:
        print(key, end=" ")