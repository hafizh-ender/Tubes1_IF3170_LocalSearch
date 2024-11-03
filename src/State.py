import numpy as np
from numba import njit

from Cube import Cube
from numba import njit

@njit
def calculate_objective_value(values, magic_number):
    dim = values.shape[0]
    conflicting = 0
    
    # Check rows
    for i in range(dim):
        for k in range(dim):
            sum_baris = np.sum(values[i, :, k])
            if sum_baris != magic_number:
                conflicting += 1

    # Check columns
    for j in range(dim):
        for k in range(dim):
            sum_kolom = np.sum(values[:, j, k])
            if sum_kolom != magic_number:
                conflicting += 1

    # Check pillars
    for i in range(dim):
        for j in range(dim):
            sum_tiang = np.sum(values[i, j, :])
            if sum_tiang != magic_number:
                conflicting += 1    
    # note : 0 tuh backward and 1 tuh maju
    # Check space diagonals
    lower_corners = [[1, 1, 1], [0, 1, 1], [0, 0, 1], [1, 0, 1]]
    for lower_corner in lower_corners:
        sum_diag_ruang = 0
        i_range = range(0, dim) if lower_corner[0] == 1 else range(dim - 1, -1, -1)
        j_range = range(0, dim) if lower_corner[1] == 1 else range(dim - 1, -1, -1)
        k_range = range(0, dim) if lower_corner[2] == 1 else range(dim - 1, -1, -1)
        
        for i, j, k in zip(i_range, j_range, k_range):
            sum_diag_ruang += values[i, j, k]
        
        if sum_diag_ruang != magic_number:
            conflicting += 1 

    # Check plane diagonals
    lower_corners = [[1, 1], [1, 0]]
    for i in range(dim):
        for lower_corner in lower_corners:
            sum_diag_bidang = 0
            for j, k in zip(range(0, dim) if lower_corner[0] == 1 else range(dim - 1, -1, -1),
                            range(0, dim) if lower_corner[1] == 1 else range(dim - 1, -1, -1)):
                sum_diag_bidang += values[i, j, k]
            if sum_diag_bidang != magic_number:
                conflicting += 1 

    for j in range(dim):
        for lower_corner in lower_corners:
            sum_diag_bidang = 0
            for i, k in zip(range(0, dim) if lower_corner[0] == 1 else range(dim - 1, -1, -1),
                            range(0, dim) if lower_corner[1] == 1 else range(dim - 1, -1, -1)):
                sum_diag_bidang += values[i, j, k]
            if sum_diag_bidang != magic_number:
                conflicting += 1 

    for k in range(dim):
        for lower_corner in lower_corners:
            sum_diag_bidang = 0
            for i, j in zip(range(0, dim) if lower_corner[0] == 1 else range(dim - 1, -1, -1),
                            range(0, dim) if lower_corner[1] == 1 else range(dim - 1, -1, -1)):
                sum_diag_bidang += values[i, j, k]
            if sum_diag_bidang != magic_number:
                conflicting += 1 
    
    return -conflicting

class State():
    def __init__(self, cube):
        self._cube = cube
        self._value = self.calculateObjectiveValue()

    # Getter and Setter for cube
    @property
    def cube(self):
        return self._cube

    @cube.setter
    def cube(self, new_cube):
        if isinstance(new_cube, Cube):
            self._cube = new_cube
            self._value = self.calculateObjectiveValue()  # Recalculate value when cube is updated
        else:
            raise ValueError("cube must be an instance of the Cube class")

    # Getter for value (no setter as it is calculated)
    @property
    def value(self):
        return self._value

    # Calculate objective value
    def calculateObjectiveValue(self):        
        return calculate_objective_value(self._cube.values, self._cube.magic_number)

