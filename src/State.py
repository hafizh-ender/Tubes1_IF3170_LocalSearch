class State:
    def __init__(self, cube):
        self._cube = cube
        self._update_objective_value()

    def _update_objective_value(self):
        from Utility import Utility

        self._objective_value = Utility.get_objective_value(self)

    @property
    def cube(self):
        return self._cube

    @property
    def objective_value(self):
        return self._objective_value

    def swap_position(self, p1: list[int], p2: list[int]):
        self._cube[tuple(p1)], self._cube[tuple(p2)] = self._cube[tuple(p2)], self._cube[tuple(p1)]

        self._update_objective_value()