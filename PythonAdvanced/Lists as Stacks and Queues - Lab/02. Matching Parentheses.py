expression = input()

parentheses =[]
for idx in range(len(expression)):
    if expression[idx] == "(":
        parentheses.append(idx)
    elif expression[idx] == ")":
        start = parentheses.pop()
        end = idx + 1
        print(expression[start:end])