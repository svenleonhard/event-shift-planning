from .planning import GAPlanning
from .fitness_calculator import FitnessCalculator

class ShiftPlanning:

    def __init__(self, preferences):
        fitness_calculator = FitnessCalculator(preferences)
        self.planner = GAPlanning(fitness_calculator)

    def plan(self):
        planning_result = self.planner.solve(20,5,8,1)
        return planning_result['Individuals'][-1]

