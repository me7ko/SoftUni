number = float(input())

if number == 0:
    print("zero")
elif number < 0:
    if -1 < number < 0:
        print("small negative")
    elif number < -1000000:
        print("large negative")
    else:
        print("negative")
elif number > 0:
    if 0 < number < 1:
        print("small positive")
    elif number > 1000000:
        print("large positive")
    elif number > 0:
        print("positive")