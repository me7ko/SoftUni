text = input()

for idx in range(len(text)):
    ch = text[idx]
    if ch == ":":
        symbol = text[idx + 1]
        print(f":{symbol}")
