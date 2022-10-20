red = 0
orange = 0
blue = 0
green = 0
max_eggs_color = ""


eggs_count = int(input())

for eggs in range(1, eggs_count + 1):
    color = input()
    if color == "red":
        red += 1
    elif color == "orange":
        orange += 1
    elif color == "blue":
        blue += 1
    elif color == "green":
        green += 1

    color_list = [red, orange, blue, green]
    if red > orange and red > blue and red > green:
        max_eggs_color = "red"
    elif orange > red and orange > blue and orange > green:
        max_eggs_color = "orange"
    elif blue > red and blue > orange and blue > green:
        max_eggs_color = "blue"
    elif green > red and green > blue and green > orange:
        max_eggs_color = "green"

print(f"Red eggs: {red}\nOrange eggs: {orange}\n"
      f"Blue eggs: {blue}\nGreen eggs: {green}\n"
      f"Max eggs: {max(color_list)} -> {max_eggs_color}")
