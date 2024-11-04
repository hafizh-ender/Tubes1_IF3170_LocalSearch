from typing import List, Optional
import numpy

from State import State

# BaseResult class with common properties and methods
class BaseResult:
    def __init__(self) -> None:
        self._state_history: List[State] = []
        self._objective_function_history: List[int] = []
        self._duration: float = 0.0 
        self._iteration: int = 0

    def add_state(self, state: State) -> None:
        """Add state to history and record its objective value."""
        self._state_history.append(state)
        self._objective_function_history.append(state.value)
        
    def export_history(self, filename: str = "state_history.txt") -> None:
        with open(filename, "w") as file:
            for i, (state, obj_value) in enumerate(zip(self._state_history, self._objective_function_history), start=1):
                file.write(f"Iteration {i}:{obj_value}\n\n")
                
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
    
    @iteration.setter
    def iteration(self, value: int) -> None:
        self._iteration = value