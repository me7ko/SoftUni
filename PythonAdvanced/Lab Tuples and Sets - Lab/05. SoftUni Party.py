reservations = set()

for _ in range(int(input())):
    reservation_code = input()
    reservations.add(reservation_code)

command = input()
while command != "END":
    reservations.remove(command)

    command = input()

print(len(reservations))
for num in sorted(reservations):
    print(num)