joinery_count = int(input())
joinery_type = input()
delivery_type = input()
price = 0

if joinery_count < 10:
    print("Invalid order")
else:
    if joinery_type == "90X130":
        if joinery_count > 60:
            price += 110 * 0.92 * joinery_count
        elif joinery_count > 30:
            price += 110 * 0.95 * joinery_count

        else:
            price += 110

    elif joinery_type == "100X150":
        if joinery_count > 80:
            price += 140 * 0.90 * joinery_count
        elif joinery_count > 40:
            price += 140 * 0.94 * joinery_count

        else:
            price += 140 * joinery_count

    elif joinery_type == "130X180":
        if joinery_count > 50:
            price += 190 * 0.88 * joinery_count
        elif joinery_count > 20:
            price += 190 * 0.93 * joinery_count

        else:
            price += 190 * joinery_count

    elif joinery_type == "200X300":
        if joinery_count > 50:
            price += 250 * 0.86 * joinery_count
        elif joinery_count > 25:
            price += 250 * 0.91 * joinery_count

        else:
            price += 250 * joinery_count

    if delivery_type == "With delivery":
        price += 60
    if joinery_count > 99:
        price *= 0.96
    print(f"{price:.2f} BGN")