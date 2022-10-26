price_dollars_processor = float(input())
price_dollars_video = float(input())
price_dollars_ram = float(input())
ram_count = int(input())
discount = float(input())

leva_processor = price_dollars_processor * 1.57
leva_processor_disc = leva_processor - (leva_processor * discount)
leva_video = (price_dollars_video * 1.57)
leva_video_disc = leva_video - (leva_video * discount)
leva_ram = (price_dollars_ram * 1.57) * ram_count

total = leva_processor_disc + leva_video_disc + leva_ram

print(f"Money needed - {total:.2f} leva.")

