total_steps = 0

init_input = input()
while init_input != "Going home":
    steps = int(init_input)
    total_steps += steps
    if total_steps >= 10000:
        break
    init_input = input()

if init_input == "Going home":
    steps_to_home = int(input())
    total_steps += steps_to_home

diff = abs(total_steps - 10000)
if total_steps >= 10000:
    print(f"Goal reached! Good job!\n{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")