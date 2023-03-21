path = input().split("\\")
split_info = path[-1].split(".")
file_name = split_info[0]
extension = split_info[1]

print(f"File name: {file_name}\nFile extension: {extension}")
