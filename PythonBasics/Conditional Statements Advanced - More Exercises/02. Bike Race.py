juniors_count = int(input())
seniors_count = int(input())
trace_type = input()

juniors = 0
seniors = 0
discount = 0
total_count = juniors_count + seniors_count

if trace_type == "trail":
    juniors += 5.50
    seniors += 7


elif trace_type == "cross-country":
    juniors += 8
    seniors += 9.50
    if total_count >= 50:
        discount = 0.25

elif trace_type == "downhill":
    juniors = 12.25
    seniors = 13.75
elif trace_type == "road":
    juniors += 20
    seniors += 21.50

result = (juniors_count * juniors) + (seniors_count * seniors)
total_result = (result - (result * 0.05)) * (1 - discount)
print(f"{total_result:.2f}")

