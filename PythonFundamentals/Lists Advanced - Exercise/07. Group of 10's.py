import math

nums = [int(num) for num in input().split(", ")]
max_value = math.ceil(max(nums) / 10)
start = 1
end = 10

for group in range(1, max_value + 1):
    lst = []
    for num in nums:
        if start <= num <= end:
            lst.append(num)
    start += 10
    end += 10
    print(f"Group of {group * 10}'s: {lst}")