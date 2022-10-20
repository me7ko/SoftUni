time_for_photos = int(input())
scenes_count = int(input())
time_per_scene = int(input())

field_preparation = time_for_photos * 0.15
filming_time = scenes_count * time_per_scene + field_preparation

diff = abs(time_for_photos - filming_time)
if time_for_photos >= filming_time:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(diff)} minutes.")