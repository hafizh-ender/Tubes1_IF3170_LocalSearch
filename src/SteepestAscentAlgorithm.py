from BaseResult import BaseResult
from BaseAlgorithm import BaseAlgorithm
from State import State
from util import Utility

from datetime import datetime

class SteepestAscentAlgorithm(BaseAlgorithm):
    @staticmethod
    def solve(initial_state: State, sideways_move: bool = False) -> BaseResult:
        """
        This function take initial_state as the input
        and output the BaseResult object obtained using
        steepest ascent algorithm
        """
        start_time = datetime.now()
        
        result = BaseResult()

        if initial_state.value == 0:
            duration = datetime.now() - start_time
            result.add_state(initial_state)
            result.duration(duration)
            return result
        else:
            current_state = initial_state
        
        while True:
            neighboor = Utility.getBestSuccessor(current_state)
            
            if not sideways_move and neighboor.value <= current_state.value:
                duration = datetime.now() - start_time
                result.duration(duration)
                return result
            if sideways_move and neighboor.value < current_state.value:
                duration = datetime.now() - start_time
                result.duration(duration)
                return result

            result.add_state(current_state)
            current_state = neighboor
