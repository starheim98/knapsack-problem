import config


# converts the list of bits into a list of the present item names
# if the bit is 1 the corresponding item's name is added to the list
def decode_knapsack(bits):
    items = []
    for i in range(len(bits)):
        if bits[i] == 1:
            item_name = config.items[i].get_name()
            items.append(item_name)
    return items

