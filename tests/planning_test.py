from context import engine
from engine import GAPlanning
import numpy as np

if __name__== "__main__":
    preferenecs = np.array([[0,1,2,2,1], [1,1,1,1,1], [2,2,0,0,0], [0,1,1,2,2], [2,1,1,1,1], [2,2,2,2,1], [1,1,2,2,1], [2,2,2,0,0]])
    planner = GAPlanning(preferenecs)
    print(planner.solve(20,5,8,1))