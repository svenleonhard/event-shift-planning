from .planning import GAPlanning
from .fitness_calculator import FitnessCalculator

class ShiftPlanning:

    def __init__(self, preferences, number_of_shifts):
        fitness_calculator = FitnessCalculator(preferences)
        self.planner = GAPlanning(fitness_calculator)

        self.number_of_employees = len(preferences)

        if self.number_of_employees > 0:
            try:
                self.number_of_tasks = len(preferences[0])
            except:
                self.number_of_tasks = 0

        self.number_of_shifts = number_of_shifts
        
    def plan(self):
        planning_result = self.planner.solve(20, self.number_of_tasks, self.number_of_shifts, self.number_of_employees,1)
        return planning_result[-1]

