nylon = 1.50
paint = 14.50
paint_tinner = 5

nylon_needed = int(input()) + 2
paint_needed = int(input()) * 1.1
paint_tinner_neeeded = int(input())
time = int(input())

sum = (nylon * nylon_needed) + (paint * paint_needed) + (paint_tinner * paint_tinner_neeeded) + 0.40
workers_cut = (sum * time)*0.3
total = sum+workers_cut
print(total)


