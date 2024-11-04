import os
from typing import List, Optional
import numpy as np

from State import State

# BaseResult class with common properties and methods
class BaseResult:
    def __init__(self) -> None:
        self._state_history: List[State] = []
        self._objective_function_history: List[int] = []
        self._duration: float = 0.0 
        self._iteration: int = 0
        self._best_state: np.ndarray = None 

    def add_state(self, state: State) -> None:
        """Add state to history and record its objective value."""
        self._state_history.append(state)
        self._objective_function_history.append(state.value)
        
    def export_history(self, filename: str = "state_history.txt") -> None:
        directory = os.path.dirname(filename)
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(filename, "w") as file:
            for i, (state, obj_value) in enumerate(zip(self._state_history, self._objective_function_history), start=1):
                file.write(f"Iteration {i}:{obj_value}:None:None\n\n" if state.previous_action is None
                           else f"Iteration {i}:{obj_value}:{"-".join(map(str, state.previous_action[0]))}:{"-".join(map(str, state.previous_action[1]))}\n\n")

                cube = state.cube 
                for frame in cube:
                    for row in frame:
                        file.write(" ".join(f"{val:.1f}" for val in row) + "\n")
                    file.write("\n")
                file.write("\n")

    @property
    def state_history(self) -> List[State]:
        return self._state_history

    @property
    def objective_function_history(self) -> List[int]:
        return self._objective_function_history

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, time: float) -> None:
        self._duration = time

    @property
    def iteration(self) -> int:
        return self._iteration

    @property
    def best_state(self) -> State:
        if not self._state_history:
            raise ValueError("State history is empty. No best state found.")
        best_state_index = self._objective_function_history.index(max(self.objective_function_history))

        return self._state_history[best_state_index]

    @iteration.setter
    def iteration(self, value: int) -> None:
        self._iteration = value
