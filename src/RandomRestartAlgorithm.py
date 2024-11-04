from State import State
from RandomRestartResult import RandomRestartResult
from BaseAlgorithm import BaseAlgorithm
from util import Utility
from Cube import Cube

from datetime import datetime

class RandomRestart(BaseAlgorithm):
    @staticmethod
    def solve(initial_state: State, max_restart: int = 299) -> RandomRestartResult:        
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
            print(current_state.value)
            neighboor = Utility.getBestSuccessor(current_state)

            if neighboor.value <= current_state.value:
                cube = Cube(dim=5)
                current_state = State(cube = cube)
                result.restart += 1

            result.add_state(current_state)
            current_state = neighboor
            result.iteration += 1 
            
            #Global maximum 
            if current_state.value == 0 or result.restart == max_restart:
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                return result
