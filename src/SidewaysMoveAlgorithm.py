from BaseAlgorithm import BaseAlgorithm
from State import State
from SidewaysMoveResult import SidewaysMoveResult
from util import Utility

from datetime import datetime


class SidewaysMoveAlgorithm(BaseAlgorithm):
    @staticmethod
    def solve(initial_state: State, max_sideways_iter: int = 250) -> SidewaysMoveResult:
        """
        This function take initial_state as the input
        and output the BaseResult object obtained using
        steepest ascent algorithm with sideways move
        """
        start_time = datetime.now()
        sideways_iter = 0
        result = SidewaysMoveResult()

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

            if neighboor.value < current_state.value:
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                return result
            if neighboor.value == current_state.value:
                sideways_iter += 1
                pass
            else: 
                sideways_iter = 0

            result.add_state(current_state)
            current_state = neighboor
            result.iteration += 1

            #Global maximum or maximum iteration for sideways move
            if current_state.value == 0 or sideways_iter == max_sideways_iter:
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                return result        
