counter = 0
num = int(input())

for n in range(1, num + 1):
    if num % n == 0:
        counter += 1
if counter > 2:
    print("False")
else:
    print("True")