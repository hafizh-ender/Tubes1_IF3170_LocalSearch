from BaseResult import BaseResult
from typing import List

# RandomRestartResult class with additional tracking for restarts and iterations
class RandomRestartResult(BaseResult):
    def __init__(self) -> None:
        super().__init__()
        self._restart: int = 0
        self._iteration_counter: int = 0
        self._iteration_per_restart: List[int] = []

    @property
    def restart(self) -> int:
        return self._restart 

    @property
    def iteration_per_restart(self) -> List[int]:
        return self._iteration_per_restart

    @BaseResult.iteration.setter
    def iteration(self, value: int) -> None:
        """Override iteration setter to track iteration counts per restart."""
        self._iteration = value
        self._iteration_counter += 1

    @restart.setter
    def restart(self, value: int) -> None:
        """Log restart and reset iteration counter."""
        self._restart = value
        self._iteration_per_restart.append(self._iteration_counter)
        self._iteration_counter = 0