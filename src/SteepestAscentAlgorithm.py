from BaseResult import BaseResult
from BaseAlgorithm import BaseAlgorithm
from State import State
from util import Utility

from datetime import datetime

class SteepestAscentAlgorithm(BaseAlgorithm):
    @staticmethod
    def solve(intial_state: State) -> BaseResult:
        """
        This function take initial_state as the input
        and output the best state obtained using
        steepest ascent algorithm
        """
        start_time = datetime.now()
        result = BaseResult()
        if current.value == 0:
            duration = start_time - datetime.now()
            result.add_state(initial_state)
            result.duration(duration)
            return result
        else:
            current_state = initial_state

        while True:
            neighboor = util.getBestSuccessor(intial_state)
            
            if neighboor.value <= current.value:
                duration = start_time - datetime.now()
                result.add_state(current_state)
                result.duration(duration)
                return result
            
            result.add_state(current_state)
            current = neighboor
