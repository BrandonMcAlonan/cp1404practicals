import random

MIN_INCREASE = 0.1
MAX_INCREASE = 0.2
MIN_DECREASE = 0.05
MAX_DECREASE = 0.25


year = 1
population = 1000
dead_gophers = 0

print("Welcome to the Gopher Population Simulator!")
print("Starting Population {}".format(population))
print(year)
while year < 11:
    population_change = 0
    dead_gophers_change = 0
    # NOT YET COMPLETED
    population_change = population * (1+(random.uniform(int(MIN_INCREASE), int(MAX_INCREASE))))
    dead_gophers_change = random.uniform(int(MIN_DECREASE), int(MAX_DECREASE))
    population = population + population_change - dead_gophers_change
    print("{} gophers were born. {} died.".format(population_change, dead_gophers_change))
    print("Year: {}".format(year))
    print("Population: {}".format(population))
    year += 1

