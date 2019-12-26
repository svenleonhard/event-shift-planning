from context import engine
from engine import ShiftPlanning
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

            shift_planning = ShiftPlanning(preferenecs, 2)

            plan = shift_planning.plan()

            logging.info(plan)

            new_dict = []
        
            for s in range(len(plan)):
                print('Shift: ', s)
                planList = []
                for i in range(len(plan[s])):
                    print('Task: ', tasks[i], 'Worker: ', workers[plan[s][i] - 1 ], " ", data[workers[plan[s][i] - 1 ]][tasks[i]])
                    name = workers[plan[s][i] - 1]

                    new_pair = {
                    'task' : tasks[i],
                    'worker' : name
                    }
                    planList.append(planList)
                shift = {
                    'shift' : s,
                    'plan' : planList
                }
                new_dict.append(shift)

            print(str(new_dict))

        

            sys.stdout.flush()
            

        except yaml.YAMLError as exc:
            print(exc)
            sys.stdout.flush()