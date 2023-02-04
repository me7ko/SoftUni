cards = input().split()
shuffle_count = int(input())

for _ in range(shuffle_count):
    first_half = cards[1:len(cards) // 2]
    second_half = cards[len(cards) // 2:-1]

    shuffled = []
    first_part_idx = 0
    second_part_idx = 0
    for idx in range(len(first_half) * 2):
        if idx % 2 == 0:
            shuffled.append(second_half[second_part_idx])
            second_part_idx += 1
        else:
            shuffled.append(first_half[first_part_idx])
            first_part_idx += 1

    cards = [cards[0]] + shuffled + [cards[-1]]

print(cards)