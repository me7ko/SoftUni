nums = [int(x) for x in input().split()]
left_car = nums[:len(nums) // 2]
right_car = nums[len(nums) // 2:]
right_car.remove(right_car[0])
right_car.reverse()

left_car_time = 0
right_car_time = 0
for left_num in left_car:
    left_car_time += left_num
    if left_num == 0:
        left_car_time *= 0.8

for right_num in right_car:
    right_car_time += right_num
    if right_num == 0:
        right_car_time *= 0.8

if right_car_time < left_car_time:
    print(f"The winner is right with total time: {right_car_time:.1f}")
else:
    print(f"The winner is left with total time: {left_car_time:.1f}")
