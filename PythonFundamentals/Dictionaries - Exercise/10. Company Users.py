info = input()

companies = {}

while info != "End":
    company, employee = info.split(" -> ")

    if company not in companies:
        companies[company] = [employee]
    if employee not in companies[company]:
        companies[company].append(employee)

    info = input()

for company,employees in companies.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")