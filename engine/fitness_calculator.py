import logging

class FitnessCalculator:

    def __init__(self, preference_matrix):
        self.preference_matrix = preference_matrix

    def calculate(self, individual):
        fitness_value = 0

        for s in range(len(individual)):
            tasks = individual[s]
            for i in range(len(tasks)):
                fitness_value = fitness_value + self.get_preference_for_worker(tasks[i], i)

        
        downtime_value = self.downtime_vektor(individual)
        fitness = fitness_value - downtime_value

        return fitness

    def downtime_vektor(self, individual):
        downtime_value = 0

        for m in range(len(self.preference_matrix)):
            employee_id = m + 1
            uptime = 0
            for s in range(len(individual)):
                tasks = individual[s]
                for i in range(len(tasks)):
                    if individual[s][i] == employee_id:
                        uptime = uptime + 1
            downtime = len(individual) - uptime
            downtime_value = downtime_value + downtime
        
        return downtime_value


    def get_preference_for_worker(self, worker_id, category):
        preference = self.preference_matrix[worker_id-1, category]
        if preference == 0:
            return -4
        return preference

    def get_list_of_prefered_employees(self, category, search_space):
        prefered_employees = []

        preference_value = 2
        while len(prefered_employees) == 0:
            for e in range(len(self.preference_matrix)):
                if self.preference_matrix[e][category] == preference_value and not self.preference_matrix[e][category] + 1 in search_space:
                    prefered_employees.append(e+1)
            preference_value = preference_value - 1
        return prefered_employees
