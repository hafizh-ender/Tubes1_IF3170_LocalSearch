from BaseAlgorithm import BaseAlgorithm
from Utility import Utility
from State import State

from StochasticHillClimbingResult import StochasticHillClimbingResult

import numpy as np
from datetime import datetime

class StochasticHillClimbingAlgorithm(BaseAlgorithm):
    @staticmethod
    def solve(initial_state: State, iteration_max: int = 1000, verbose: bool = False) -> StochasticHillClimbingResult:
        start_time = datetime.now()
        
        current_state = initial_state
        result = StochasticHillClimbingResult()
        
        while True:
            if verbose:
                print(f"Iteration: {result.iteration}. Value: {current_state.value}")
            
            result.add_state(state=current_state)
            
            # Terminate if global maximum is reached or maximum iteration is reached
            if current_state.value == 0 or result.iteration == iteration_max:
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                
                return result
            
            neighbour_state = Utility.getRandomSuccessor(current_state)
            
            if neighbour_state.value > current_state.value:
                current_state = neighbour_state
            
            result.iteration += 1