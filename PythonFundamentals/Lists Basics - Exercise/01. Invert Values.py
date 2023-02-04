nums = input().split()

inverted = []
for idx in range(len(nums)):
    inverted.append(-int(nums[idx]))

print(inverted)