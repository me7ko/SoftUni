first_word, second_word = input().split()
result = 0
min_len = min(len(first_word), len(second_word))

for idx in range(min_len):
    result += ord(first_word[idx]) * ord(second_word[idx])

for idx in range(min_len, len(first_word)):
    result += ord(first_word[idx])

for idx in range(min_len, len(second_word)):
    result += ord(second_word[idx])

print(result)