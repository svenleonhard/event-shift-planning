from context import engine
from engine import ShiftPlanning
import numpy as np
import yaml, sys

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

            shift_planning = ShiftPlanning(preferenecs)

            plan = shift_planning.plan()

            new_dict = []
            for i in range(len(plan)):
                print('Task: ', tasks[i], 'Worker: ', workers[plan[i] - 1 ])
                name = workers[plan[i] - 1]
                new_pair = {
                    'task' : tasks[i],
                    'worker' : name
                }

                new_dict.append(new_pair)

            print(str(new_dict))
            sys.stdout.flush()
            

        except yaml.YAMLError as exc:
            print(exc)
            sys.stdout.flush()