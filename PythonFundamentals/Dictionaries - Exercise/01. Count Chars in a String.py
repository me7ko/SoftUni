text = input().split()

data = {}

for word in text:
    for letter in word:
        if letter not in data:
            data[letter] = 1
        else:
            data[letter] += 1

for letter, count in data.items():
    print(f"{letter} -> {count}")