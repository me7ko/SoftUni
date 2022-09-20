budget = float(input())
videocards_count = int(input())
processors_count = int(input())
ram_count = int(input())

total_videos = videocards_count * 250
total_processors = (total_videos * 0.35) * processors_count
total_ram = (total_videos * 0.1) * ram_count

all_total = total_videos + total_processors + total_ram

if videocards_count > processors_count:
    all_total = all_total * 0.85
diff = abs(budget - all_total)

if budget >= all_total:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")