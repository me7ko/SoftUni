from math import pi
figure = input()

if figure == "square":
    a = float(input())
    area = a * a
    print(f"{area:.3f}")
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")
elif figure == "circle":
    r = float(input())
    area = pi * (r ** 2)
    print(f"{area:.3f}")
elif figure == "triangle":
    b = float(input())
    h = float(input())
    area = 1/2 * b * h
    print(f"{area:.3f}")