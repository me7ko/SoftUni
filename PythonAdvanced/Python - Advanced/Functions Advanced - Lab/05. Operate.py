from functools import reduce


def operate(operator, *args):
    return reduce(lambda a, b: eval(f"{a}{operator}{b}"), args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))