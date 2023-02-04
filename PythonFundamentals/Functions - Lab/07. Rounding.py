lst = [float(n) for n in input().split()]


def rounding(numbers):
    rounded = [round(n) for n in numbers]
    return rounded


print(rounding(lst))