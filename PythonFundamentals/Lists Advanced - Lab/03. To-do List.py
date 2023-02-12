to_do_str = input()
final_lst = [0] * 10
while to_do_str != "End":
    split_to_do = to_do_str.split("-")
    priority = int(split_to_do[0]) - 1
    note = split_to_do[1]
    final_lst.pop(priority)
    final_lst.insert(priority, note)

    to_do_str = input()
print([letter for letter in final_lst if letter != 0])