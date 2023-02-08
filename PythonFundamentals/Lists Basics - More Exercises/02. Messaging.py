numbers = [n for n in input().split()]
text = input()

message = ""
for num in numbers:
    index = sum([int(s_num) for s_num in num])
    if index >= len(text):
        index = index - len(text)
    message += text[index]
    text = text[:index] + text[index + 1:]

print(message)