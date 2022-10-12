c = 0
o = 0
n = 0
first_word = ""
final_word = ""

symbol = input()
while symbol != "End":
    if symbol.isalpha():
        if symbol == "c":
            c += 1
            if c >= 2:
                first_word += symbol
        elif symbol == "o":
            o += 1
            if o >= 2:
                first_word += symbol
        elif symbol == "n":
            n += 1
            if n >= 2:
                first_word += symbol
        else:
            first_word += symbol
        if c >= 1 and o >= 1 and n >= 1:
            final_word += first_word + " "
            first_word = ""
            c = 0
            o = 0
            n = 0

    symbol = input()

print(final_word)
