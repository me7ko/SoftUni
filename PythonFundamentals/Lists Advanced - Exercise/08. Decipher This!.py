secret_message = input().split()

words = []
numbers = []
for word in secret_message:
    num = ""
    letter = ""
    for symbol in word:
        if symbol.isdigit():
            num += symbol
        else:
            letter += symbol
    numbers.append(int(num))
    if len(letter) != 1:
        letter = f"{letter[-1]}{letter[1:-1]}{letter[0]}"
    words.append(letter)

for first, second in zip(numbers, words):
    print(f"{chr(first)}{second}", end=" ")