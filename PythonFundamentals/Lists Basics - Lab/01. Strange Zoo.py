whole_body = []

for _ in range(3):
    body_part = input()
    whole_body.append(body_part)

whole_body[0], whole_body[2] = whole_body[2], whole_body[0]
print(whole_body)