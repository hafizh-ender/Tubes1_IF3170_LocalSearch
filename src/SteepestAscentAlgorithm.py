from BaseAlgorithm import BaseAlgorithm
from SteepestAscentResult import SteepestAscentResult
from State import State
from Utility import Utility

from datetime import datetime

class SteepestAscentAlgorithm(BaseAlgorithm):
    @staticmethod
    def solve(initial_state: State, verbose: bool = False):
        """
        This function take initial_state as the input
        and output the BaseResult object obtained using
        steepest ascent algorithm
        """
        start_time = datetime.now()
        
        current_state = initial_state
        result = SteepestAscentResult()
        
        while True:
            if verbose:
                print(f"Iteration: {result.iteration}. Value: {current_state.value}")
            
            result.add_state(current_state)
            
            # Terminate if global maximum is reached
            if current_state.value == 0:
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                
                return result
                
            neighboor = Utility.getBestSuccessor(current_state)

            if neighboor.value <= current_state.value:
                # Terminate if no neighbor is better
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                
                return result
            
            current_state = neighboor
            result.iteration += 1
            
