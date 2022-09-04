deposit_sum = float(input())
time_deposit = int(input())
year_procent = float(input())/100

sum = deposit_sum + time_deposit * ((deposit_sum * year_procent) / 12)
print(sum)