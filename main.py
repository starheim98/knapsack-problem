import time

from Item import Item
from functions.ConvergenceCheck import convergence_check
from functions.Crossover import crossover
from functions.DecodeKnapsack import decode_knapsack
import config
from functions.Survival import survival
from functions.GeneratePopulation import generate_pop, generate_pop
from functions.Mutation import mutate_pop
from functions.SelectParents import select_parents_uniform, select_parents_roulette
import matplotlib.pyplot as plt


def main():
    # timer
    start = time.time()

    # knapsack
    max_weight = 1000
    config.max_weight = max_weight
    item_list = config.items

    # GA parameters
    chromosome_size = len(item_list)
    population_size = 2000
    mutation_rate = 0.05
    survival_rate = 0.5  # percent of population that is passed on to the next generation
    elitism = 50  # do not mutate the fittest individuals
    keep = int(population_size * survival_rate)
    number_of_matings = int((population_size - keep) / 2)

    # initial population
    generation_counter = 1
    repetitions = 0
    population = generate_pop(population_size, chromosome_size)
    highest_fitness, best_solution = convergence_check(population)

    # stopping criteria
    max_iterations = 1000
    max_fitness = 12600

    # plotting data
    fitness_data = []
    x_axis = []

    # iterate generations
    while generation_counter <= max_iterations and highest_fitness < max_fitness:

        population = survival(population, keep)
        offsprings = []

        for i in range(number_of_matings):
            parent1, parent2 = select_parents_roulette(population)
            offspring1, offspring2 = crossover(parent1, parent2)
            offsprings.append(offspring1)
            offsprings.append(offspring2)

        # next generation
        population.extend(offsprings)
        population = mutate_pop(population, mutation_rate, elitism)
        highest_fitness, new_solution = convergence_check(population)

        if new_solution == best_solution:
            repetitions += 1
        else:
            repetitions = 0

        # increase exploration if the solutions are repetitive
        if repetitions >= 10:
            mutation_rate = 0.2
        elif repetitions >= 5:
            mutation_rate = 0.1
        else:
            mutation_rate = 0.05

        best_solution = new_solution
        print("Generation:", generation_counter, " \t highest fitness:", highest_fitness,
              "\tbest solution: ", decode_knapsack(best_solution))

        fitness_data.append(highest_fitness)
        x_axis.append(generation_counter)
        generation_counter += 1

    end = time.time()
    time_spent = round((end - start), 2)
    if highest_fitness == max_fitness:
        print("\nFound optimal solution in ", time_spent, " seconds, after ",
              generation_counter - 1, "generations")
        print("The correct answer was: ", decode_knapsack(best_solution))
    else:
        print("Did not find the optimal solution")

    # plot results
    plt.plot(x_axis, fitness_data)
    plt.xlabel("Generations")
    plt.ylabel("Highest fitness")
    plt.show()


if __name__ == '__main__':
    main()
