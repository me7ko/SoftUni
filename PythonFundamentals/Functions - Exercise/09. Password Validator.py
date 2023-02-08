def is_len_valid(password):
    return 6 <= len(password) <= 10


def is_only_letters_and_digits(password):
    flag = password.isalnum()
    return flag


def does_password_have_2_digits(password):
    counter = 0
    for ch in password:
        if ch.isdigit():
            counter += 1
    return counter >= 2


is_valid = True
password = input()
if not is_len_valid(password):
    print("Password must be between 6 and 10 characters")
    is_valid = False
if not is_only_letters_and_digits(password):
    print("Password must consist only of letters and digits")
    is_valid = False
if not does_password_have_2_digits(password):
    print("Password must have at least 2 digits")
    is_valid = False
if is_valid:
    print("Password is valid")