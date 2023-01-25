lines = int(input())
word = input()
lst = []
filtered_lst = []

for _ in range(lines):
    command = input()
    lst.append(command)
    if word in command:
        filtered_lst.append(command)
print(lst)

print(filtered_lst)