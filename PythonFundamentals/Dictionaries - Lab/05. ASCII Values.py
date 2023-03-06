characters = input().split(", ")

ascii_dict = {}

for char in characters:
    ascii_dict[char] = ord(char)

print(ascii_dict)