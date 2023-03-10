data = input()

letters = []
digits = []
symbols = []

for let in data:
    if let.isdigit():
        digits.append(let)
    elif let.isalpha():
        letters.append(let)
    else:
        symbols.append(let)

print(*digits,sep="")
print(*letters, sep="")
print(*symbols, sep="")