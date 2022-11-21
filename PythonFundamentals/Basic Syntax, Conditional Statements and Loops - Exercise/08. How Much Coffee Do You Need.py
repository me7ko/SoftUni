coffee_count = 0
lower_letters = ["coding", "cat", "dog", "movie"]
higher_letters = ["CODING", "CAT", "DOG", "MOVIE"]

command = input()
while command != "END":
    if command in lower_letters:
        coffee_count += 1
    elif command in higher_letters:
        coffee_count += 2

    command = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)