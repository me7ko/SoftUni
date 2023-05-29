def print_numbers(positive, negative):
    print(positive)
    print(negative)

    if abs(negative) > positive:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
positive_numbers = sum(x for x in numbers if x > 0)
negative_numbers = sum(x for x in numbers if x < 0)

print_numbers(positive_numbers, negative_numbers)