card = input().split()
A = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
B = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
flag = False

for idx in range(len(card)):
    if card[idx] in A:
        A.remove(card[idx])
    if card[idx] in B:
        B.remove(card[idx])
    if len(A) < 7 or len(B) < 7:
        flag = True
        break

print(f"Team A - {len(A)}; Team B - {len(B)}")
if flag:
    print("Game was terminated")