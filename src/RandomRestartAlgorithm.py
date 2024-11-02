from SteepestAscentAlgorithm import SteepestAscentAlgorithm as steep
from State import State
from BaseResult import BaseResult

class RandomRestart(steep):
    @staticmethod
    def solve(initial_state: State) -> BaseResult:        
        """
        This function take initial_state as the input
        and output the BaseResult object obtained using
        random restart algorithm
        """
        return super().solve(initial_state, random_restart = True)        
