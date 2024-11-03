import numpy as np
import copy

from Cube import Cube

class State:
    def __init__(self, cube: Cube):
        self._cube = cube
        self._value = self.calculateObjectiveValue()

    def __lt__(self, other):
        return self._value < other._value

    def __le__(self, other):
        return self._value <= other._value

    def __eq__(self, other):
        return self._value == other._value

    def __ne__(self, other):
        return self._value != other._value

    def __gt__(self, other):
        return self._value > other._value

    def __ge__(self, other):
        return self._value >= other._value

    @property
    def cube(self):
        return self._cube

    @cube.setter
    def cube(self, new_cube: Cube):
        self._cube = new_cube
        self._value = self.calculateObjectiveValue()  # Recalculate value when cube is updated
        
    @property
    def value(self):
        return self._value

    # Calculate objective value
    def calculateObjectiveValue(self) -> int:        
        dim = self._cube.dim
        magic_number = self._cube.magic_number

        # Convert values to a numpy array for efficient slicing and summation
        values = np.array(self._cube.values)

        # Initialize conflict count
        conflicting = 0

        # Check row sums (across the x-axis), column sums (y-axis), and pillar sums (z-axis)
        row_sums = values.sum(axis=2)
        col_sums = values.sum(axis=0)
        pillar_sums = values.sum(axis=1)

        # Count conflicts for rows, columns, and pillars
        conflicting += np.sum(row_sums != magic_number)
        conflicting += np.sum(col_sums != magic_number)
        conflicting += np.sum(pillar_sums != magic_number)

        # Space diagonals
        if np.trace(values, axis1=0, axis2=1).sum() != magic_number:
            conflicting += 1
        if np.trace(values[::-1], axis1=0, axis2=1).sum() != magic_number:
            conflicting += 1
        if np.trace(values[:, ::-1, :]).sum() != magic_number:
            conflicting += 1
        if np.trace(values[:, :, ::-1]).sum() != magic_number:
            conflicting += 1

        # Plane diagonals in xy, yz, and xz planes (forward and reverse)
        for i in range(dim):
            if values[i].diagonal().sum() != magic_number:  # xy-plane
                conflicting += 1
            if values[:, i, :].diagonal().sum() != magic_number:  # yz-plane
                conflicting += 1
            if values[:, :, i].diagonal().sum() != magic_number:  # xz-plane
                conflicting += 1
            if values[i, :, ::-1].diagonal().sum() != magic_number:  # xy-plane, reverse
                conflicting += 1
            if values[:, i, ::-1].diagonal().sum() != magic_number:  # yz-plane, reverse
                conflicting += 1
            if values[::-1, :, i].diagonal().sum() != magic_number:  # xz-plane, reverse
                conflicting += 1

        return -conflicting
