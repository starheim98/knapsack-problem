import config


# calculates the fitness of a knapsack based on the items value in the knapsack
# if the total weight exceeds the max_weight tolerance, 0 is returned.
def fitness(knapsack, max_weight):
    item_list = config.items
    weight = 0
    fitness = 0

    for i in range(len(knapsack)):
        if knapsack[i] == 1:
            weight += item_list[i].get_weight()
            fitness += item_list[i].get_value()

            # return 0 if the item combination is more than max limit
            if weight > max_weight:
                return 0
    return fitness
