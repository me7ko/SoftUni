number_of_electrons = int(input())
n = 1
lst_of_electrons = []
while number_of_electrons > 0:
    shell = min(2 * n**2, number_of_electrons)
    lst_of_electrons.append(shell)
    n += 1
    number_of_electrons -= shell
print(lst_of_electrons)