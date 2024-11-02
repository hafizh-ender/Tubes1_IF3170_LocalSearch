from typing import List
from State import State
class BaseResult:
    def __init__(self) -> None:
        self._state_history: List[State] = []
        self._objective_function_history: List[int] = []
        self._duration: float = 0.0 

    def add_state(self, state: State) -> None:
        self._state_history.append(state)
        self._objective_function_history.append(state.objective_value)

    @property
    def state_history(self) -> State:
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
