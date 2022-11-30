first_string = input()
second_string = input()
init_first_string = first_string

for ch in range(len(first_string)):
    first_word = second_string[:ch + 1]
    second_word = first_string[ch + 1:]
    final_word = first_word + second_word
    if init_first_string == final_word:
        continue
    init_first_string = final_word
    print(final_word)