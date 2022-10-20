import math

n = int(input())
total_points = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
others = 0

for _ in range(1, n + 1):
    color = input()

    if color == "red":
        total_points += 5
        red += 1
    elif color == "orange":
        total_points += 10
        orange += 1
    elif color == "yellow":
        total_points += 15
        yellow += 1
    elif color == "white":
        total_points += 20
        white += 1
    elif color == "black":
        total_points = math.floor(total_points / 2)
        black += 1
    else:
        others += 1

print(f"Total points: {total_points}\nRed balls: {red}\nOrange balls: {orange}\n"
      f"Yellow balls: {yellow}\nWhite balls: {white}\nOther colors picked: {others}\n"
      f"Divides from black balls: {black}")