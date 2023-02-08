def is_palindrome(num_as_str):
    return num_as_str == num_as_str[::-1]


nums = [int(x) for x in input().split(", ")]

for n in nums:
    print(is_palindrome(str(n)))