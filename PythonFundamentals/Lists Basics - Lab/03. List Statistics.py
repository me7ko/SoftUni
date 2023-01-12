lines = int(input())

positive_num = []
negative_num = []

for _ in range(lines):
    current_number = int(input())
    if current_number >= 0:
        positive_num.append(current_number)
    else:
        negative_num.append(current_number)

print(positive_num)
print(negative_num)
print(f"Count of positives: {len(positive_num)}")
print(f"Sum of negatives: {sum(negative_num)}")