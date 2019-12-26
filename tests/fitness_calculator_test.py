from context import engine
from engine import FitnessCalculator
import numpy as np
import yaml, sys, logging

if __name__== "__main__":

    with open("worker.yml", 'r') as stream:
        try:
            data = yaml.safe_load(stream)

            workers = list(data.keys())
            tasks = []
            for task in data[workers[0]]:
                tasks.append(task)

            preference_matrix = []
            for worker in data:
                worker_preferences = []

                for task in tasks:
                    worker_preferences.append(data[worker][task])

                preference_matrix.append(worker_preferences)
            print(preference_matrix)

            preferenecs = np.array(preference_matrix)

            fitness_calculator = FitnessCalculator(preferenecs)

            individual = [[2, 6, 5, 4, 1], [5, 8, 3, 2, 4]]

            fitness = fitness_calculator.calculate(individual)

            logging.info('Fitness: %s', fitness)
        

            sys.stdout.flush()
            

        except yaml.YAMLError as exc:
            print(exc)
            sys.stdout.flush()