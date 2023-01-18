word = input()
upper = []
for letter in range(len(word)):
    if word[letter].isupper():
        upper.append(letter)
print(upper)