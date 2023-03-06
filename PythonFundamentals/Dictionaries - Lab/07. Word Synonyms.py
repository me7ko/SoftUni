lines = int(input())

word_synonyms = {}

for _ in range(lines):
    word = input()
    synonym = input()
    if word not in word_synonyms:
        word_synonyms[word] = [synonym]
    else:
        word_synonyms[word].append(synonym)

for word, synonym in word_synonyms.items():
    print(f"{word} - {', '.join(synonym)}")