kilometers = int(input())
day_or_night = input()


if day_or_night == "day":
    if 0 < kilometers < 20:
        taxi_price = 0.70 + (kilometers * 0.79)
        print(f"{taxi_price:.2f}")
    elif kilometers >= 100:
        train_price = kilometers * 0.06
        print(f"{train_price:.2f}")
    else:
        bus_price = kilometers * 0.09
        print(f"{bus_price:.2f}")

elif day_or_night == "night":
    if 0 < kilometers < 20:
        taxi_price = 0.70 + (kilometers * 0.90)
        print(f"{taxi_price:.2f}")
    elif kilometers >= 100:
        train_price = kilometers * 0.06
        print(f"{train_price:.2f}")
    else:
        bus_price = kilometers * 0.09
        print(f"{bus_price:.2f}")


