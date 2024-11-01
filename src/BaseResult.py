class BaseResult:
    def __init__(self):
        self._state_history = []
        self._objective_function_history = []
        self._duration = None

    def add_state(self, state):
        self._state_history.append(state)
        self._objective_function_history.append(state.value)

    @property
    def state_history(self):
        return self._state_history

    @property
    def objective_function_history(self):
        return self._objective_function_history

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value