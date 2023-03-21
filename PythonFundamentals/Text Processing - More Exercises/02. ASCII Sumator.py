start_char = input()
end_char = input()
text = input()

sum = 0
for letter in text:
    if ord(start_char) < ord(letter) < ord(end_char):
        sum += ord(letter)

print(sum)