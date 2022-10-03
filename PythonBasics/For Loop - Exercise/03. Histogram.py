number = int(input())
p_1 = 0
p_2 = 0
p_3 = 0
p_4 = 0
p_5 = 0
for num in range(1, number + 1):
    percentages = int(input())

    if percentages < 200:
        p_1 += 1
    elif percentages < 400:
        p_2 += 1
    elif percentages < 600:
        p_3 += 1
    elif percentages < 800:
        p_4 += 1
    else:
        p_5 += 1
percentage_p_1 = p_1 / number * 100
print(f"{percentage_p_1:.2f}%")
percentage_p_2 = p_2 / number * 100
print(f"{percentage_p_2:.2f}%")
percentage_p_3 = p_3 / number * 100
print(f"{percentage_p_3:.2f}%")
percentage_p_4 = p_4 / number * 100
print(f"{percentage_p_4:.2f}%")
percentage_p_5 = p_5 / number * 100
print(f"{percentage_p_5:.2f}%")
