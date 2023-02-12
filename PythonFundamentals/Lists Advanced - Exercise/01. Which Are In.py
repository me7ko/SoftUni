substr = input().split(", ")
sequence = input().split(", ")

lst_of_sequences = []
for sub in substr:
    for seq in sequence:
        if sub in seq:
            lst_of_sequences.append(sub)
            break

print(lst_of_sequences)