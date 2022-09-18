import math

h = float(input())
w = float(input())

columns = math.trunc((w * 100 - 100) / 70)
rows = math.trunc((h * 100 / 120))
result = math.trunc((columns * rows) - 3)

print(result)
