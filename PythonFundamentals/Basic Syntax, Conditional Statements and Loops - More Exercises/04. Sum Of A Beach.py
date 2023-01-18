counter = 0
txt = input().lower()

counter += txt.count("sand")
counter += txt.count("water")
counter += txt.count("fish")
counter += txt.count("sun")

print(counter)