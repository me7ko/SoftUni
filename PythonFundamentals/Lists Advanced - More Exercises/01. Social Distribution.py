population = [int(x) for x in input().split(", ")]
min_wealth = int(input())

if min_wealth > sum(population) / len(population):
    print("No equal distribution possible")
    exit()

while any(x < min_wealth for x in population):
    max_number = max(population)
    min_num = min(population)

    index_max = population.index(max_number)
    index_min = population.index(min_num)
    added_value = min_wealth - min_num

    population[index_max] -= added_value
    population[index_min] += added_value

print(population)