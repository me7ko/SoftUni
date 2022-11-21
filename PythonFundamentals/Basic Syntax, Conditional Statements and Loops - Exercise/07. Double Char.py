word = ""
command = input()

while command != "End":
    if command == "SoftUni":
        command = input()
        continue

    for i in command:
        word += i * 2
        
    print(word)
    word = ""
    command = input()
