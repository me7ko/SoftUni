total_tickets = 0
student_ticket = 0
standard_ticket = 0
kids_ticket = 0


movie_name = input()
while movie_name != "Finish":
    total = 0
    init_free_seats = int(input())

    ticket_type = input()
    while True:
        if ticket_type == "student":
            student_ticket += 1
        elif ticket_type == "standard":
            standard_ticket += 1
        elif ticket_type == "kid":
            kids_ticket += 1

        if ticket_type == "Finish" or total == init_free_seats:
            print(f"{movie_name} - {((total / init_free_seats) * 100):.2f}% full.")
            movie_name = ticket_type
            break
        elif ticket_type == "End":
            print(f"{movie_name} - {((total / init_free_seats) * 100):.2f}% full.")
            movie_name = input()
            break

        total_tickets += 1
        total += 1

        ticket_type = input()

print(f"Total tickets: {total_tickets}")
print(f"{((student_ticket / total_tickets) * 100):.2f}% student tickets.")
print(f"{((standard_ticket / total_tickets) * 100):.2f}% standard tickets.")
print(f"{((kids_ticket / total_tickets) * 100):.2f}% kids tickets.")
