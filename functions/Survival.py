import functools
import config
from functions.Fitness import fitness


# sorts the population based on fitness and keeps the most fit chromosomes
def survival(population, keep):
    sorted_population = sorted(population, key=functools.cmp_to_key(compare), reverse=True)
    return sorted_population[:keep]


# compares the fitness of two chromosomes
# function is used to sort the population
def compare(x, y):
    max_weight = config.max_weight
    return fitness(x, max_weight) - fitness(y, max_weight)
