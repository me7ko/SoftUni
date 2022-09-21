v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

first_tube = p1 * h
second_tube = p2 * h
total_tubes = first_tube + second_tube

result = (total_tubes * 100) / v
first_procent = (first_tube * 100) / total_tubes
second_procent = (second_tube * 100) / total_tubes
remaining = total_tubes - v

if total_tubes <= v:
    print(f"The pool is {result}% full. Pipe 1: {first_procent:.2f}%. Pipe 2: {second_procent:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {remaining:.2f} liters.")

