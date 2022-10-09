name = input()
init_password = input()

while True:
    password = input()

    if init_password == password:
        print(f"Welcome {name}!")
        break
