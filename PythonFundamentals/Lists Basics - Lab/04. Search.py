lines = int(input())
word = input()
lst = []

for _ in range(lines):
    command = input()
    lst.append(command)
print(lst)

for i in range(len(lst) - 1, -1, -1):
    if word not in lst[i]:
        lst.remove(lst[i])
print(lst)