import random
import config


# mutates a population except elite individuals
def mutate_pop(population, mutation_rate, elitism):
    elite_individuals = elitism
    # keep elite individuals
    new_population = population[:elite_individuals]
    mutable_population = population[elite_individuals:]
    for chromosome in mutable_population:
        new_population.append(mutate_individual(chromosome, mutation_rate))

    return new_population


# iterates over a chromosome's genes and flips the bit if
#       a random number between 0 and 1 is less or equal to the mutation rate
def mutate_individual(individual, mutation_rate):
    for i in range(len(individual)):
        randint = random.random()
        if randint <= mutation_rate:
            individual[i] = 1 - individual[i]
    return individual
