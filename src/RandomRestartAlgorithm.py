from State import State
from RandomRestartResult import RandomRestartResult
from BaseAlgorithm import BaseAlgorithm
from Utility import Utility

from datetime import datetime

class RandomRestart(BaseAlgorithm):
    @staticmethod
    def solve(initial_state: State, max_restart: int = 299, verbose: bool = False) -> RandomRestartResult:        
        """
        This function take initial_state as the input
        and output the BaseResult object obtained using
        random restart algorithm
        """
        start_time = datetime.now()
        
        current_state = initial_state
        result = RandomRestartResult()
        
        while True:
            if verbose:
                print(f"Iteration: {result.iteration}. Value: {current_state.value}. Restart: {result.restart}")
            
            result.add_state(current_state)
            
            # Terminate if global maximum is reached
            if current_state.value == 0:
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                
                return result 
            
            neighboor = Utility.getBestSuccessor(current_state)

            if neighboor.value <= current_state.value:
                # Terminate if no neighbor is better and maximum restart has concluded
                if result.restart == max_restart:
                    duration = datetime.now() - start_time
                    result.duration = duration.total_seconds()
                    
                    return result 
                else:
                    neighboor = State(dim=5)
                    
                    result.restart += 1

            current_state = neighboor
            result.iteration += 1 