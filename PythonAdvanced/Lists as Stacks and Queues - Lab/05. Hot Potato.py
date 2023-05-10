from collections import deque

kids = deque(input().split())
n_toss = int(input())

while len(kids) > 1:
    for toss in range(1, n_toss + 1):
        kids.rotate(-1)
    print(f"Removed {kids.pop()}")

print(f"Last is {kids[-1]}")

