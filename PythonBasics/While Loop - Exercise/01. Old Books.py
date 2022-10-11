checked_books = 0
flag = False
book_to_find = input()

current_book = input()
while current_book != "No More Books":
    checked_books += 1
    if current_book == book_to_find:
        checked_books -= 1
        flag = True
        break
    current_book = input()
if flag:
    print(f"You checked {checked_books} books and found it.")
else:
    print(f"The book you search is not here!\nYou checked {checked_books} books.")