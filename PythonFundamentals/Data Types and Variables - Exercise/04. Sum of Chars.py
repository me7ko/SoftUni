lines = int(input())

summ = 0
for _ in range(lines):
    letter = input()
    summ += ord(letter)

print(f"The sum equals: {summ}")