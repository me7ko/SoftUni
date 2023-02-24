class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []


    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        self._Zoo__animals += 1


    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}"


name = input()
n = int(input())

zoo = Zoo(name)
for _ in range(1, n + 1):
    species, name = input().split()
    zoo.add_animal(species, name)


species_to_print = input()
print(zoo.get_info(species_to_print))
print(f"Total animals: {zoo._Zoo__animals}")