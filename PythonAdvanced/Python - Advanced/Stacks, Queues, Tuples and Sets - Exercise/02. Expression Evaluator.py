import math
from collections import deque

expression = deque(input().split())
current_index = 0

while current_index < len(expression):
    symbol = expression[current_index]

    if symbol == "*":
        for _ in range(current_index - 1):
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif symbol == "/":
        for _ in range(current_index - 1):
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
    elif symbol == "+":
        for _ in range(current_index - 1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
    elif symbol == "-":
        for _ in range(current_index - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))

    if symbol in "*/+-":
        del expression[1]
        current_index = 1

    current_index += 1

print(math.floor(*expression))