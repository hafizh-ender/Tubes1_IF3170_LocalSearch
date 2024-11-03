from BaseResult import BaseResult
from typing import List

class RandomRestartResult(BaseResult):
    def __init__(self) -> None:
        super().__init__()
        self._iteration: int = 0
        self._restart: int = 0
        self._iteration_counter: int = 0
        self._iteration_per_restart: List[int] = []

    @property
    def iteration(self) -> int:
        return self._iteration

    @property
    def restart(self) -> int:
        return self._restart 

    @property
    def iteration_restart(self) -> List[int]:
        return self._iteration_restart

    @iteration.setter
    def iteration(self, value: int) -> None:
        self._iteration = value
        self._iteration_counter += 1


    @restart.setter
    def restart(self, value: int) -> None:
        self._restart = value
        self._iteration_per_restart.append(self._iteration_counter)
        self._iteration_counter = 0
