def get_data_type(command, inp):
    if command == "int":
        int_res = int(inp) * 2
        print(int_res)
    elif command == "real":
        real_res = float(inp) * 1.5
        print(f"{real_res:.2f}")
    elif command == "string":
        print(f"${inp}$")


command = input()
inp = input()
get_data_type(command, inp)