counter = 0

first_letter = input()
second_letter = input()
third_letter = input()

first_ord = ord(first_letter)
second_ord = ord(second_letter)
third_ord = ord(third_letter)

for f_letter in range(first_ord, second_ord + 1):
    for s_letter in range(first_ord, second_ord + 1):
        for t_letter in range(first_ord, second_ord + 1):
            if f_letter != third_ord and s_letter != third_ord and t_letter != third_ord:
                counter += 1
                print(f"{chr(f_letter)}{chr(s_letter)}{chr(t_letter)}", end=" ")

print(counter)