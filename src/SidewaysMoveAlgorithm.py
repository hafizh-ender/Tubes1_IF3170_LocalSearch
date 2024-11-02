from SteepestAscentAlgorithm import SteepestAscentAlgorithm
from State import State

class SidewaysMoveAlgorithm(SteepestAscentAlgorithm):
    @staticmethod
    def solve(intial_state: State) -> BaseResult:
        """
        This function take initial_state as the input
        and output the BaseResult object obtained using
        steepest ascent algorithm with sideways move
        """
        return super().solve(initial_state: State, sideways_move = True)
