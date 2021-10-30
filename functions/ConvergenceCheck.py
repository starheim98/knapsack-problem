import config
from functions.Fitness import fitness


# returns the best solution and its fitness number of a population
def convergence_check(population):
    max_weight = config.max_weight
    highest_fitness = 0
    best_solution = []

    for knapsack in population:
        result = fitness(knapsack, max_weight)
        if result > highest_fitness:
            highest_fitness = result
            best_solution = knapsack

    return highest_fitness, best_solution
