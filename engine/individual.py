class Individual:

    def __init__(self, genstring, fitness):
        self.genstring = genstring
        self.fitness = fitness

    def copy(self):
        return Individual(self.genstring, self.fitness)
