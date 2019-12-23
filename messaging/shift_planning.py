from context import engine
from engine import ShiftPlanning
import numpy as np
import yaml, sys, json, logging

def make_plan(planConfig):
    if 1==1:
        planConfigDictString = planConfig.decode("utf-8", "ignore")
        logging.info(planConfigDictString)

        planConfigDict = json.loads(planConfigDictString)
        employees = planConfigDict['employees']
        categories = planConfigDict['categories']

        preference_matrix = []
        for employee in employees:

            if len(employee['rating']) == len(categories):
                employee_preferences = []

                for ratingItem in employee['rating']:
                    employee_preferences.append(ratingItem['rating'])

                preference_matrix.append(employee_preferences)


        print(preference_matrix)

        preferenecs = np.array(preference_matrix)

        shift_planning = ShiftPlanning(preferenecs)

        plan = shift_planning.plan()

        new_dict = []
        for i in range(len(plan)):
                    
            name = employees[plan[i] - 1]['employee']['name']
            category = categories[i]['description']
            new_pair = {
                'category' : category,
                'assignee' : name
                    }

            new_dict.append(new_pair)
        
        print(new_dict)
                    
        return new_dict