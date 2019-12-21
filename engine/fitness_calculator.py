class FitnessCalculator:

    def __init__(self, preference_matrix):
        self.preference_matrix = preference_matrix

    def calculate(self, individual):
        fitness_value = 0
        for i in range(len(individual)):
            fitness_value = fitness_value + self.get_preference_for_worker(individual[i], i)**2

        return fitness_value

    def get_preference_for_worker(self, worker_id, category):
        return self.preference_matrix[worker_id-1, category]