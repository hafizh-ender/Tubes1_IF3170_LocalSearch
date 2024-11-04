import numpy as np
from typing import List

from numba import njit

@njit
def calculateObjectiveValueNumba(dim, magic_number, cube) -> int:
    conflict = 0
    
    # Check rows
    for i in range(dim):
        for k in range(dim):
            sum_baris = np.sum(cube[i, :, k])
            if sum_baris != magic_number:
                conflict += 1
    # Check columns
    for j in range(dim):
        for k in range(dim):
            sum_kolom = np.sum(cube[:, j, k])
            if sum_kolom != magic_number:
                conflict += 1
    # Check pillars
    for i in range(dim):
        for j in range(dim):
            sum_tiang = np.sum(cube[i, j, :])
            if sum_tiang != magic_number:
                conflict += 1    
    # note : 0 tuh backward and 1 tuh maju
    # Check space diagonals
    lower_corners = [[1, 1, 1], [0, 1, 1], [0, 0, 1], [1, 0, 1]]
    for lower_corner in lower_corners:
        sum_diag_ruang = 0
        i_range = range(0, dim) if lower_corner[0] == 1 else range(dim - 1, -1, -1)
        j_range = range(0, dim) if lower_corner[1] == 1 else range(dim - 1, -1, -1)
        k_range = range(0, dim) if lower_corner[2] == 1 else range(dim - 1, -1, -1)
        
        for i, j, k in zip(i_range, j_range, k_range):
            sum_diag_ruang += cube[i, j, k]
        
        if sum_diag_ruang != magic_number:
            conflict += 1 
    # Check plane diagonals
    lower_corners = [[1, 1], [1, 0]]
    for i in range(dim):
        for lower_corner in lower_corners:
            sum_diag_bidang = 0
            for j, k in zip(range(0, dim) if lower_corner[0] == 1 else range(dim - 1, -1, -1),
                            range(0, dim) if lower_corner[1] == 1 else range(dim - 1, -1, -1)):
                sum_diag_bidang += cube[i, j, k]
            if sum_diag_bidang != magic_number:
                conflict += 1 
    for j in range(dim):
        for lower_corner in lower_corners:
            sum_diag_bidang = 0
            for i, k in zip(range(0, dim) if lower_corner[0] == 1 else range(dim - 1, -1, -1),
                            range(0, dim) if lower_corner[1] == 1 else range(dim - 1, -1, -1)):
                sum_diag_bidang += cube[i, j, k]
            if sum_diag_bidang != magic_number:
                conflict += 1 
    for k in range(dim):
        for lower_corner in lower_corners:
            sum_diag_bidang = 0
            for i, j in zip(range(0, dim) if lower_corner[0] == 1 else range(dim - 1, -1, -1),
                            range(0, dim) if lower_corner[1] == 1 else range(dim - 1, -1, -1)):
                sum_diag_bidang += cube[i, j, k]
            if sum_diag_bidang != magic_number:
                conflict += 1 
    
    return -conflict

    # conflict = 0
    
    # # pillar, column, row
    # conflict += np.sum(cube.sum(axis=0) != magic_number) # Check pillar
    # conflict += np.sum(cube.sum(axis=1) != magic_number) # Check column
    # conflict += np.sum(cube.sum(axis=2) != magic_number) # Check row
    
    # # plane diagonal
    # conflict += np.sum(np.sum(np.diagonal(cube, axis1=1, axis2=2), axis=1) != magic_number) # Check column x row plane
    # conflict += np.sum(np.sum(np.diagonal(cube, axis1=0, axis2=2), axis=1) != magic_number) # Check pillar x row plane
    # conflict += np.sum(np.sum(np.diagonal(cube, axis1=0, axis2=1), axis=1) != magic_number) # Check pillar x column plane

    # # plane anti-diagonal
    # conflict += np.sum(np.sum(np.diagonal(np.flip(cube, axis=1), axis1=1, axis2=2), axis=1) != magic_number) # Check column x row plane
    # conflict += np.sum(np.sum(np.diagonal(np.flip(cube, axis=0), axis1=0, axis2=2), axis=1) != magic_number) # Check pillar x row plane
    # conflict += np.sum(np.sum(np.diagonal(np.flip(cube, axis=0), axis1=0, axis2=1), axis=1) != magic_number) # Check pillar x column plane

    # # space diagonal
    # conflict += np.sum(np.diagonal(np.diagonal(cube))) != magic_number # Check 0,0,0 to dim,dim,dim diagonal
    # conflict += np.sum(np.diagonal(np.flip(np.diagonal(cube), axis=0)))!= magic_number # Check 0,0,dim to dim,dim,0
    # conflict += np.sum(np.diagonal(np.diagonal(np.flip(cube, axis=1))))!= magic_number # Check dim,0,0 to 0,dim,dim
    # conflict += np.sum(np.diagonal(np.flip(np.diagonal(np.flip(cube, axis=1)), axis=0)))!= magic_number # dim,0,dim to 0,dim,0

    # return -conflict

class State:
    def __init__(self, cube: np.ndarray = None, previous_action: List[List[int]] = None, dim: int = 5):
        if cube is not None:
            self._cube = cube
            self._dim = cube.shape[0]
        else:
            self._cube = np.arange(1, dim ** 3 + 1)
            np.random.shuffle(self._cube)
            self._cube = np.reshape(self._cube, (dim, dim, dim))
            self._dim = dim
            
        self._magic_number = self._dim * (self._dim ** 3 + 1) / 2
        self._value = self.calculateObjectiveValue()
        self._previous_action = previous_action

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

    def __copy__(self):
        new_copy = State(cube=self.cube.copy())
        return new_copy
    
    @property
    def dim(self) -> int:
        return self._dim

    @property
    def magic_number(self) -> float:
        return self._magic_number

    @property
    def cube(self) -> np.ndarray:
        return self._cube

    @cube.setter
    def cube(self, new_cube: np.ndarray) -> None:
        self._cube = new_cube
        self._value = self.calculateObjectiveValue()  # Recalculate value when cube is updated

    @property
    def previous_action(self):
        return self._previous_action

    @previous_action.setter
    def previous_action(self, new_previous_action: List[List[int]]):
        self._previous_action = new_previous_action
        
    @property
    def value(self) -> int:
        return self._value
    
    
    # Calculate objective value
    def calculateObjectiveValue(self) -> int:  
        dim = self.dim
        magic_number = self.magic_number
        cube = self.cube
        
        return calculateObjectiveValueNumba(dim, magic_number, cube)