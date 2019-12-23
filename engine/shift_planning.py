from .planning import GAPlanning
from .fitness_calculator import FitnessCalculator

class ShiftPlanning:

    def __init__(self, preferences):
        fitness_calculator = FitnessCalculator(preferences)
        self.planner = GAPlanning(fitness_calculator)

        self.number_of_employees = len(preferences)

        if self.number_of_employees > 0:
            try:
                self.number_of_tasks = len(preferences[0])
            except:
                self.number_of_tasks = 0
        
    def plan(self):
        planning_result = self.planner.solve(20, self.number_of_tasks, self.number_of_employees,1)
        return planning_result['Individuals'][-1]

