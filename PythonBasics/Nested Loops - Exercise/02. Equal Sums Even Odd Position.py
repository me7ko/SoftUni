start_number = int(input())
last_number = int(input())

for num in range(start_number, last_number + 1):
    hundred_thousand = num // 100000
    ten_thousand = (num // 10000) % 10
    thousand = (num // 1000) % 10
    hundred = (num // 100) % 10
    tens = (num // 10) % 10
    units = num % 10

    odd_sum = hundred_thousand + thousand + tens
    even_sum = ten_thousand + hundred + units

    if odd_sum == even_sum:
        print(num, end=" ")