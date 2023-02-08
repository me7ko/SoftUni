def char_range(start, end):
    characters = []
    for char in range(ord(start) + 1, ord(end)):
        characters.append(chr(char))
    return characters


start = input()
end = input()

print(" ".join(char_range(start, end)))