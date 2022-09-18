x = float(input())
y = float(input())
h = float(input())

side_wall = x * y
window = 2.25
result_1 = 2 * side_wall - 2 * window

back_wall = x * x
entry = 2.4
result_2 = 2 * back_wall - entry

total_area1 = result_1 + result_2

green_paint = total_area1 / 3.4
print(f"{green_paint:.2f}")

roofs = 2 * (x * y)
triangles = 2 * (x * h / 2)
total_area2 = roofs + triangles
red_paint = total_area2 / 4.3
print(f"{red_paint:.2f}")