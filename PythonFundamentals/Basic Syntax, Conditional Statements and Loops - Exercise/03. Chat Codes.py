num = int(input())

for n in range(1, num + 1):
    number = int(input())
    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number != 88 and number != 86 and number < 88:
        print("GREAT!")
    elif number > 88:
        print("Bye.")