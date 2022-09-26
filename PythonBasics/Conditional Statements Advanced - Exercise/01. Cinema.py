projection_type = input()
rows = int(input())
columns = int(input())
price = 0

if projection_type == "Premiere":
    price = 12 * (rows * columns)
elif projection_type == "Normal":
    price = 7.5 * (rows * columns)
elif projection_type == "Discount":
    price = 5 * (rows * columns)

print(f"{price:.2f} leva")