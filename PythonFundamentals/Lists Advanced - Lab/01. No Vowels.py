lst = [letter for letter in input() if letter.lower() not in ["a", "o", "u", "e", "i"]]
print("".join(lst))