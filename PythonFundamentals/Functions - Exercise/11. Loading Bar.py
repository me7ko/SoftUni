def get_loading_bar(number_as_str):
    loading_bar = ["."] * 10
    for n in number_as_str:
        n = int(n)
        idx = n - 1
        for i in range(idx + 1):
            loading_bar[i] = "%"
        break
    return loading_bar


num = input()
if num != "100":
    print(f"{num}% [{''.join(get_loading_bar(num))}]\nStill loading...")
else:
    print(f"100% Complete!\n[%%%%%%%%%%]")