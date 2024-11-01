import numpy as np
import copy

from Cube import Cube

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
        conflicting = 0
        
        # Check rows
        for i in range(self._cube.dim):
            for k in range(self._cube.dim):
                sum_baris = sum(self._cube.values[i][j][k] for j in range(self._cube.dim))
                if sum_baris != self._cube.magic_number:
                    conflicting += 1
        
        # Check columns
        for j in range(self._cube.dim):
            for k in range(self._cube.dim):
                sum_kolom = sum(self._cube.values[i][j][k] for i in range(self._cube.dim))
                if sum_kolom != self._cube.magic_number:
                    conflicting += 1
        
        # Check pillars
        for i in range(self._cube.dim):
            for j in range(self._cube.dim):
                sum_tiang = sum(self._cube.values[i][j][k] for k in range(self._cube.dim))
                if sum_tiang != self._cube.magic_number:
                    conflicting += 1    
                    
        # Check space diagonals
        lower_corners = [[1,1,1],[self._cube.dim,1,1],[self._cube.dim,self._cube.dim,1],[1,self._cube.dim,1]]
        for lower_corner in lower_corners:
            sum_diag_ruang = 0
            i_range = range(0, self._cube.dim) if lower_corner[0] == 1 else range(self._cube.dim-1, -1, -1)
            j_range = range(0, self._cube.dim) if lower_corner[1] == 1 else range(self._cube.dim-1, -1, -1)
            k_range = range(0, self._cube.dim) if lower_corner[2] == 1 else range(self._cube.dim-1, -1, -1)
            
            for i, j, k in zip(i_range, j_range, k_range):
                sum_diag_ruang += self._cube.values[i][j][k]
            
            if sum_diag_ruang != self._cube.magic_number:
                conflicting += 1 
        
        # Check plane diagonals
        lower_corners = [[1,1],[1,self._cube.dim]]
        for i in range(self._cube.dim):
            for lower_corner in lower_corners:
                sum_diag_bidang = sum(self._cube.values[i][j][k] for j, k in zip(
                    range(0, self._cube.dim) if lower_corner[0] == 1 else range(self._cube.dim-1, -1, -1),
                    range(0, self._cube.dim) if lower_corner[1] == 1 else range(self._cube.dim-1, -1, -1)
                ))
                if sum_diag_bidang != self._cube.magic_number:
                    conflicting += 1 
                                
        for j in range(self._cube.dim):
            for lower_corner in lower_corners:
                sum_diag_bidang = sum(self._cube.values[i][j][k] for i, k in zip(
                    range(0, self._cube.dim) if lower_corner[0] == 1 else range(self._cube.dim-1, -1, -1),
                    range(0, self._cube.dim) if lower_corner[1] == 1 else range(self._cube.dim-1, -1, -1)
                ))
                if sum_diag_bidang != self._cube.magic_number:
                    conflicting += 1 
                    
        for k in range(self._cube.dim):
            for lower_corner in lower_corners:
                sum_diag_bidang = sum(self._cube.values[i][j][k] for j, i in zip(
                    range(0, self._cube.dim) if lower_corner[0] == 1 else range(self._cube.dim-1, -1, -1),
                    range(0, self._cube.dim) if lower_corner[1] == 1 else range(self._cube.dim-1, -1, -1)
                ))
                if sum_diag_bidang != self._cube.magic_number:
                    conflicting += 1 
            
        return -conflicting
