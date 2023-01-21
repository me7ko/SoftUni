key = int(input())
lines = int(input())

word = ""
for _ in range(lines):
    letter = input()
    ascii_num = ord(letter) + key
    ascii_letter = chr(ascii_num)
    word += ascii_letter
print(word)