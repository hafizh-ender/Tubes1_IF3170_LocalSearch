from BaseAlgorithm import BaseAlgorithm
from StochasticHillClimbingResult import StochasticHillClimbingResult
from Utility import Utility

import numpy as np

from datetime import datetime

class StochasticHillClimbingAlgorithm(BaseAlgorithm):
    @staticmethod
    def solve(initial_state, iteration_max=1000, verbose=False):
        start_time = datetime.now()
        
        current_state = initial_state
        
        result = StochasticHillClimbingResult()
        result.iteration = iteration_max
        
        for iteration in range(iteration_max):
            if verbose:
                print(f"Iteration: {iteration}. Value: {current_state.value}")
            
            result.add_state(state=current_state)
            
            neighbour_state = Utility.getRandomSuccessor(current_state)
            
            if neighbour_state.value > current_state.value:
                current_state = neighbour_state
                
        duration = datetime.now() - start_time
            
        result.duration = duration.total_seconds()
        return result