number = float(input())

while number >= 0:
    final_number = number * 2
    print(f"Result: {final_number:.2f}")
    number = float(input())
else:
    print("Negative number!")