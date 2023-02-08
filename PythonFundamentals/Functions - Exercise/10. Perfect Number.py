def get_perfect_num(num):
    divisors = []
    for cur_num in range(1 , num):
        if num % cur_num == 0:
            divisors.append(cur_num)
    return sum(divisors) == num


num = int(input())

if get_perfect_num(num):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")