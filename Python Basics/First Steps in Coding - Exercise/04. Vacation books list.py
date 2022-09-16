from math import floor
numbers_of_page = int(input())
pages_for_hour = int(input())
days= int(input())

hours = numbers_of_page / pages_for_hour
print(floor(hours/days))
