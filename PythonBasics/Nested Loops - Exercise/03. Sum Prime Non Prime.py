counter = 0
prime = 0
non_prime = 0

num = input()
while num != "stop":
    num = int(num)

    if num < 0:
        print("Number is negative.")
        num = input()
        continue

    counter = 0
    for n in range(1, num + 1):
        if num % n == 0:
            counter += 1
    if counter > 2:
        non_prime += num
    elif counter == 2:
        prime += num

    num = input()

print(f"Sum of all prime numbers is: {prime}\nSum of all non prime numbers is: {non_prime}")