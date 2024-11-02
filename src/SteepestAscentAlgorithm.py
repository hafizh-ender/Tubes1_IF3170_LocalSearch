from BaseAlgorithm import BaseAlgorithm
from SteepestAscentResult import SteepestAscentResult
from State import State
from util import Utility

from datetime import datetime

class SteepestAscentAlgorithm(BaseAlgorithm):
    @staticmethod
    def solve(initial_state: State):
        """
        This function take initial_state as the input
        and output the BaseResult object obtained using
        steepest ascent algorithm
        """
        start_time = datetime.now()
        result = SteepestAscentResult()

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
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                return result

            result.add_state(current_state)
            current_state = neighboor
            result.iteration += 1
            
            #Global maximum 
            if current_state.value == 0:
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                return result
