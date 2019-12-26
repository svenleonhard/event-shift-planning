from .planning import GAPlanning
from .fitness_calculator import FitnessCalculator

class ShiftPlanning:

    def __init__(self, preferences, number_of_shifts):
        self.fitness_calculator = FitnessCalculator(preferences)
        self.planner = GAPlanning(self.fitness_calculator)

        self.number_of_employees = len(preferences)

        if self.number_of_employees > 0:
            try:
                self.number_of_tasks = len(preferences[0])
            except:
                self.number_of_tasks = 0

        self.number_of_shifts = number_of_shifts
        
    def plan(self):

        best_plan = self.planner.solve(12, self.number_of_tasks, self.number_of_shifts, self.number_of_employees,1)
        for i in range(5):
            next_plan = self.planner.solve(12, self.number_of_tasks, self.number_of_shifts, self.number_of_employees,1)
            if next_plan.fitness > best_plan.fitness:
                best_plan = next_plan

        return best_plan

