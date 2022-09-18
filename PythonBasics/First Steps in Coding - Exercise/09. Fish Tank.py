length = int(input())
width = int(input())
height = int(input())
procent = float(input())/100

volume = length * width * height
volume_in_litres = volume / 1000
needed_litres = volume_in_litres * (1 - procent)
print(needed_litres)
