from State import State
from RandomRestartResult import RandomRestartResult
from BaseAlgorithm import BaseAlgorithm
from Utility import Utility

from datetime import datetime

class RandomRestart(BaseAlgorithm):
    @staticmethod
    def solve(initial_state: State, max_restart: int = 20, verbose: bool = False) -> RandomRestartResult:        
        """
        This function take initial_state as the input
        and output the BaseResult object obtained using
        random restart algorithm
        """
        start_time = datetime.now()
        result = RandomRestartResult()

        if initial_state.value == 0:
            duration = datetime.now() - start_time
            result.add_state(initial_state)
            result.duration = duration.total_seconds()
            return result
        else:
            current_state = initial_state
        
        while True:
            if verbose:
                print(f"Iteration: {result.iteration}. Value: {current_state.value}. Restart: {result.restart}")
            
            neighboor = Utility.getBestSuccessor(current_state)

            if neighboor.value <= current_state.value:
                neighboor = Utility.getRandomSuccessor(current_state)
                result.restart += 1

            result.add_state(current_state)
            current_state = neighboor
            result.iteration += 1 
            
            #Global maximum 
            if current_state.value == 0 or result.restart == max_restart:
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                return result
