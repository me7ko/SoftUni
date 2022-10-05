period = int(input())

treated_patients = 0
untreated_patients = 0
doctors = 7

for days in range(1, period + 1):
    patients_count = int(input())

    if days % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1

    if patients_count < doctors:
        treated_patients += patients_count
    else:
        untreated_patients += patients_count - doctors
        treated_patients += doctors
doctors = 7
print(f"Treated patients: {treated_patients}.\nUntreated patients: {untreated_patients}.")