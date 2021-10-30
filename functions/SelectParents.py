import random
import numpy as np


# selects parents with weighted randomness based on rank
# in my solution the population is already sorted at this point
#       no need to sort again
def select_parents_roulette(population):
    possible_parents = len(population)
    # creates an array with number between the size of population and 0.
    # the array is an probability distribution used to select parents
    weights = np.linspace(possible_parents, 1, possible_parents)

    # return two random individuals from the population based on their weight
    return random.choices(population, weights=weights, k=2)


# randomly uniform parent selection, no weighted bias
def select_parents_uniform(population):
    parent1 = population[random.randint(0, len(population) - 1)]
    parent2 = population[random.randint(0, len(population) - 1)]
    return parent1, parent2
