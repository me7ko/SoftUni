class Party:
    def __init__(self):
        self.people = []


names = input()
party = Party()

while names != "End":
    party.people.append(names)

    names = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")