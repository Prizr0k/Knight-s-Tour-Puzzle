# our class Ship
class Ship:
    def __init__(self, name, capacity, countre):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.countre = countre

    # the old sail method that you need to rewrite
    def sailed(self):
        print(f"The {self.name} has sailed for {self.countre}!")

c = input()
black_pearl = Ship("Black Pearl", 800, c)
black_pearl.sailed()
