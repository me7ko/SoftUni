exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

total_exam_min = (exam_hour * 60) + exam_minute
total_arrival_min = (arrival_hour * 60) + arrival_minute

diff_min = abs(total_arrival_min - total_exam_min)
if total_arrival_min > total_exam_min:
    print("Late")
    if diff_min >= 60:
        hour = diff_min // 60
        minute = diff_min % 60
        print(f"{hour}:{minute:02d} hours after the start")
    else:
        print(f"{diff_min} minutes after the start")
elif total_arrival_min == total_exam_min or diff_min <= 30:
    print("On time")
    if diff_min > 0:
        hour = diff_min // 60
        minute = diff_min % 60
        print(f"{diff_min} minutes before the start")
else:
    print("Early")
    if diff_min < 60:
        hour = diff_min // 60
        minute = diff_min % 60
        print(f"{diff_min} minutes before the start")
    else:
        hour = diff_min // 60
        minute = diff_min % 60
        print(f"{hour}:{minute:02d} hours before the start")