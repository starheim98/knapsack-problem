import random


# generates a population of a given size
def generate_pop(pop_size, number_of_items):
    population = []
    for i in range(pop_size):
        population.append(generate_chromosome(number_of_items))

    return population


# generates a list of 0's and 1's with the length of available items
def generate_chromosome(number_of_items):
    return random.choices([0, 1], k=number_of_items)

