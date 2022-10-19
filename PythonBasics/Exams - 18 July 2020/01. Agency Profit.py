name = input()
adults_ticket_count = int(input())
kids_ticket_count = int(input())
adult_ticket_price = float(input())
tax = float(input())

kid_ticket_price = adult_ticket_price * 0.3
total_adult_ticket_price = adult_ticket_price + tax
total_kid_ticket_price = kid_ticket_price + tax
all_total = (kids_ticket_count * total_kid_ticket_price + adults_ticket_count * total_adult_ticket_price) * 0.2

print(f"The profit of your agency from {name} tickets is {all_total:.2f} lv.")