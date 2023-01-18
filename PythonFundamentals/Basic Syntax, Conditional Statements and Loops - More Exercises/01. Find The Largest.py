number = input()

largest_num = []

for n in number:
    largest_num.append(n)

largest_num.sort()
largest_num.reverse()

print(''.join(largest_num))