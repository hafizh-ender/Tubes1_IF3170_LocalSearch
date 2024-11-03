from BaseResult import BaseResult

import numpy as np

class StochasticHillClimbingResult(BaseResult):
    def __init__(self):
        super().__init__()
        self._iteration = None

    @property
    def iteration(self) -> int:
        return self._iteration
    
    @iteration.setter
    def iteration(self, value: int) -> None:
        self._iteration = value