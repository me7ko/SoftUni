flag = False
total_pieces = 0

length = int(input())
width = int(input())

init_pieces = length * width
pieces = init_pieces

input_line = input()
while input_line != "STOP":
    pieces_taken = int(input_line)
    total_pieces += pieces_taken
    pieces -= pieces_taken
    if pieces <= 0:
        flag = True
        break
    input_line = input()

diff = abs(init_pieces - total_pieces)
if flag:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")