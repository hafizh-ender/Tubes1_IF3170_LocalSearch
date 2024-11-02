from BaseResult import BaseResult

class SteepestAscentResult(BaseResult):
    def __init__(self) -> None:
        super().__init__()
        self._iteration = 0

    @property
    def iteration(self):
        return self._iteration
    
    @iteration.setter
    def iteration(self, value: int):
        self._iteration = value
