reverse_word = ""
word = input()

for letter in word:
    reverse_word += letter

print(reverse_word[::-1])