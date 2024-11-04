from BaseAlgorithm import BaseAlgorithm
from State import State
from SidewaysMoveResult import SidewaysMoveResult
from Utility import Utility

from datetime import datetime


class SidewaysMoveAlgorithm(BaseAlgorithm):
    @staticmethod
    def solve(initial_state: State, max_sideways_iter: int = 250, verbose: bool = False) -> SidewaysMoveResult:
        """
        This function take initial_state as the input
        and output the BaseResult object obtained using
        steepest ascent algorithm with sideways move
        """
        start_time = datetime.now()
        
        current_state = initial_state
        result = SidewaysMoveResult()
        
        sideways_iter = 0
        
        while True:
            if verbose:
                print(f"Iteration: {result.iteration}. Value: {current_state.value}. Sideways Move: {sideways_iter}")
                
            result.add_state(current_state)
            
            # Terminate if global maximum is reached
            if current_state.value == 0:
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                
                return result    
            
            neighboor = Utility.getBestSuccessor(current_state)

            if neighboor.value < current_state.value:
                # Terminate if all neighbor is worse
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                
                return result
            if neighboor.value == current_state.value:
                # Terminate if best neighbor has the same value and max sideway move is reached
                if sideways_iter == max_sideways_iter:
                    duration = datetime.now() - start_time
                    result.duration = duration.total_seconds()
                    
                    return result
                else:
                    sideways_iter += 1
            else: 
                sideways_iter = 0

            current_state = neighboor
            result.iteration += 1

