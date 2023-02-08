def get_odd_and_even_sum(number_as_str):
    even_sum = 0
    odd_sum = 0
    for num in number_as_str:
        num = int(num)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return [odd_sum, even_sum]


num_as_str = input()

result = get_odd_and_even_sum(num_as_str)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")