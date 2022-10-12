c = 0
o = 0
n = 0
current_word = ""
final_word = ""

symbol = input()
while symbol != "End":
    if symbol.isalpha():
        if symbol == "c":
            c += 1
            if c >= 2:
                current_word += symbol
        elif symbol == "o":
            o += 1
            if o >= 2:
                current_word += symbol
        elif symbol == "n":
            n += 1
            if n >= 2:
                current_word += symbol
        else:
            current_word += symbol
        if c >= 1 and o >= 1 and n >= 1:
            final_word += current_word + " "
            current_word = ""
            c = 0
            o = 0
            n = 0

    symbol = input()

print(final_word)
