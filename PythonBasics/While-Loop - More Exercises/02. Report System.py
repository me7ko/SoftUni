total_money = 0
counter = 0
cash = 0
cash_counter = 0
credit_card = 0
credit_counter = 0

total_sum = int(input())

init_input = input()
while init_input != "End":
    product = int(init_input)
    counter += 1

    if counter % 2 == 0:
        if product < 10:
            print("Error in transaction!")
        else:
            credit_card += product
            credit_counter += 1
            total_money += product
            print("Product sold!")
    else:
        if product > 100:
            print("Error in transaction!")
        else:
            cash += product
            cash_counter += 1
            total_money += product
            print("Product sold!")

    if total_money >= total_sum:
        print(f"Average CS: {cash/cash_counter:.2f}\nAverage CC: {credit_card/credit_counter:.2f}")
        break

    init_input = input()
    
else:
    print("Failed to collect required money for charity.")