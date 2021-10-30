
class Item:

    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value
