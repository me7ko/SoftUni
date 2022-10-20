first_line = int(input())
second_line = int(input())

thousand_first = first_line // 1000
hundred_first = (first_line // 100) % 10
ten_first = (first_line // 10) % 10
unit_first = first_line % 10

thousand_second = second_line // 1000
hundred_second = (second_line // 100) % 10
ten_second = (second_line // 10) % 10
unit_second = second_line % 10

for thousand in range(thousand_first, thousand_second + 1):
    for hundred in range(hundred_first, hundred_second + 1):
        for ten in range(ten_first, ten_second + 1):
            for unit in range(unit_first, unit_second + 1):
                if thousand % 2 != 0 and hundred % 2 != 0 and ten % 2 != 0 and unit % 2 != 0:
                    print(f"{thousand}{hundred}{ten}{unit}", end=" ")