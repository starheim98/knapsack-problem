import random


# Generates a random crossover point to divide the parents genes into two parts
# returns two offsprings as a result of combining the gene parts
def crossover(parent1, parent2):
    chromosome_length = len(parent1)
    crossover_point = random.randint(1, chromosome_length - 1)
    parent1_genes = (parent1[:crossover_point], parent1[crossover_point:])
    parent2_genes = (parent2[:crossover_point], parent2[crossover_point:])
    offspring1 = parent1_genes[0] + parent2_genes[1]
    offspring2 = parent2_genes[0] + parent1_genes[1]
    return offspring1, offspring2

