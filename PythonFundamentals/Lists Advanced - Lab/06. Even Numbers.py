nums = [int(x) for x in input().split(", ")]
print([index for index in range(len(nums)) if nums[index] % 2 == 0])