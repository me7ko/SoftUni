budget = float(input())
video_card_count = int(input())
processor_count = int(input())
ram_count = int(input())
discount = 0

video_card = 250
video_card_sum = video_card * video_card_count

processor = video_card_sum * 0.35
processor_sum = processor * processor_count

ram = video_card_sum * 0.10
ram_sum = ram * ram_count

total_sum = video_card_sum + processor_sum + ram_sum

if video_card_count > processor_count:
    discount = 0.15

final_price = total_sum * (1 - discount)

if budget >= final_price:
    print(f"You have {budget - final_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {final_price - budget:.2f} leva more!")