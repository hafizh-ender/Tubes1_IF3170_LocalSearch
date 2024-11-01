from BaseResult import BaseResult
import numpy as np

class StochasticHillClimbingResult(BaseResult):
    def __init__(self):
        super().__init__()
        self._iteration = None

    def add_state(self, state):
        super().add_state(state)

    @property
    def iteration(self):
        return self._iteration
    
    @iteration.setter
    def iteration(self, value):
        self._iteration = value
    
    