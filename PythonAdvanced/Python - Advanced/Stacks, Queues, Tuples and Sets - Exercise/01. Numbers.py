first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    command, sequence, *data = input().split()

    if command + " " + sequence == "Add First":
        for num in data:
            first_sequence.add(int(num))

    elif command + " " + sequence == "Add Second":
        for num in data:
            second_sequence.add(int(num))

    elif command + " " + sequence == "Remove First":
        for num in data:
            if int(num) in first_sequence:
                first_sequence.remove(int(num))

    elif command + " " + sequence == "Remove Second":
        for num in data:
            if int(num) in second_sequence:
                second_sequence.remove(int(num))

    elif command + " " + sequence == "Check Subset":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")