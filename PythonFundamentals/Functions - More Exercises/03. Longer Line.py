import math

x1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y1 = math.floor(float(input()))
y2 = math.floor(float(input()))
x3 = math.floor(float(input()))
x4 = math.floor(float(input()))
y3 = math.floor(float(input()))
y4 = math.floor(float(input()))

first_x = math.floor(abs(x1) + abs(x2))
first_y = math.floor(abs(y1) + abs(y2))
second_x = math.floor(abs(x3) + abs(x4))
second_y = math.floor(abs(y3) + abs(y4))


def get_closer(first_x, first_y, second_x, second_y):
    first = first_x + first_y
    second = second_x + second_y
    if first > second:
        if abs(x1) + abs(x2) > abs(y1) + abs(y2):
            return f"({y1}, {y2})({x1}, {x2})"
        else:
            return f"({x1}, {x2})({y1}, {y2})"

    elif first < second:
        if abs(x3) + abs(x4) > abs(y3) + abs(y4):
            return f"({y3}, {y4})({x3}, {x4})"
        else:
            return f"({x3}, {x4})({y3}, {y4})"

    else:
        if abs(x3) + abs(x4) > abs(y3) + abs(y4):
            return f"({y3}, {y4})({x3}, {x4})"
        else:
            return f"({x3}, {x4})({y3}, {y4})"


print(get_closer(first_x, first_y, second_x, second_y))