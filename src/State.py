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
    def cube(self) -> Cube:
        return self._cube

    @cube.setter
    def cube(self, new_cube: Cube) -> None:
        self._cube = new_cube
        self._value = self.calculateObjectiveValue()  # Recalculate value when cube is updated
        
    @property
    def value(self) -> int:
        return self._value

    # Calculate objective value
    def calculateObjectiveValue(self) -> int:  
        dim = self.cube.dim
        magic_number = self.cube.magic_number
        values = self.cube.values

        conflict = 0
        
        # pillar, column, row
        conflict += np.sum(values.sum(axis=0) != magic_number) # Check pillar
        conflict += np.sum(values.sum(axis=1) != magic_number) # Check column
        conflict += np.sum(values.sum(axis=2) != magic_number) # Check row
        
        # plane diagonal
        conflict += np.sum(np.sum(np.diagonal(values, axis1=1, axis2=2), axis=1) != magic_number) # Check column x row plane
        conflict += np.sum(np.sum(np.diagonal(values, axis1=0, axis2=2), axis=1) != magic_number) # Check pillar x row plane
        conflict += np.sum(np.sum(np.diagonal(values, axis1=0, axis2=1), axis=1) != magic_number) # Check pillar x column plane

        # plane anti-diagonal
        conflict += np.sum(np.sum(np.diagonal(np.flip(values, axis=1), axis1=1, axis2=2), axis=1) != magic_number) # Check column x row plane
        conflict += np.sum(np.sum(np.diagonal(np.flip(values, axis=0), axis1=0, axis2=2), axis=1) != magic_number) # Check pillar x row plane
        conflict += np.sum(np.sum(np.diagonal(np.flip(values, axis=0), axis1=0, axis2=1), axis=1) != magic_number) # Check pillar x column plane

        # space diagonal
        conflict += np.sum(np.diagonal(np.diagonal(values))) != magic_number # Check 0,0,0 to dim,dim,dim diagonal
        conflict += np.sum(np.diagonal(np.flip(np.diagonal(values), axis=0)))!= magic_number # Check 0,0,dim to dim,dim,0
        conflict += np.sum(np.diagonal(np.diagonal(np.flip(values, axis=1))))!= magic_number # Check dim,0,0 to 0,dim,dim
        conflict += np.sum(np.diagonal(np.flip(np.diagonal(np.flip(values, axis=1)), axis=0)))!= magic_number # dim,0,dim to 0,dim,0

        return -conflict
    
        # dim = self._cube.dim
        # magic_number = self._cube.magic_number
        
        # conflicting = 0
         
        # # Cek baris
        # for i in range(dim):
        #     for k in range(dim):
        #         sum_baris = 0
        #         for j in range(dim):
        #             sum_baris += self._cube.values[i][j][k]
                
        #         if sum_baris != magic_number:
        #             conflicting += 1
        
        # # Cek kolom
        # for j in range(dim):
        #     for k in range(dim):
        #         sum_kolom = 0
        #         for i in range(dim):
        #             sum_kolom += self._cube.values[i][j][k]
                
        #         if sum_kolom != magic_number:
        #             conflicting += 1
        
        # # Cek tiang
        # for i in range(dim):
        #     for j in range(dim):
        #         sum_tiang = 0
        #         for k in range(dim):
        #             sum_tiang += self._cube.values[i][j][k]

        #         if sum_tiang != magic_number:
        #             conflicting += 1    
                    
        # # Cek diagonal ruang
        # lower_corners = [[1,1,1],[dim,1,1],[dim,dim,1],[1,dim,1]]
        # for lower_corner in lower_corners:
        #     sum_diag_ruang = 0
        #     i_lower = lower_corner[0]
        #     j_lower = lower_corner[1]
        #     k_lower = lower_corner[2]
            
        #     i_range = range(0,dim) if i_lower == 1 else range(dim-1,-1,-1)
        #     j_range = range(0,dim) if j_lower == 1 else range(dim-1,-1,-1)
        #     k_range = range(0,dim) if k_lower == 1 else range(dim-1,-1,-1)
            
        #     for i, j, k in list(zip(i_range, j_range, k_range)):
        #         sum_diag_ruang += self._cube.values[i][j][k]
            
        #     if sum_diag_ruang != magic_number:
        #         conflicting += 1 
        
        # # Cek potongan diagonal bidang
        # magic_diag_bidang = 6*dim
        # lower_corners = [[1,1],[1,dim],]
        # for i in range(dim):
        #     for lower_corner in lower_corners:
        #         sum_diag_bidang = 0
        #         j_lower = lower_corner[0]
        #         k_lower = lower_corner[1]
                
        #         j_range = range(0,dim) if j_lower == 1 else range(dim-1,-1,-1)
        #         k_range = range(0,dim) if k_lower == 1 else range(dim-1,-1,-1)
                
        #         for j, k in list(zip(j_range, k_range)):
        #             sum_diag_bidang += self._cube.values[i][j][k]
            
        #         if sum_diag_bidang != magic_number:
        #             conflicting += 1 
                                
        # for j in range(dim):
        #     for lower_corner in lower_corners:
        #         sum_diag_bidang = 0
        #         i_lower = lower_corner[0]
        #         k_lower = lower_corner[1]
                
        #         i_range = range(0,dim) if i_lower == 1 else range(dim-1,-1,-1)
        #         k_range = range(0,dim) if k_lower == 1 else range(dim-1,-1,-1)
                
        #         for i, k in list(zip(i_range, k_range)):
        #             sum_diag_bidang += self._cube.values[i][j][k]
                
        #         if sum_diag_bidang != magic_number:
        #             conflicting += 1 
                    
        # for k in range(dim):
        #     for lower_corner in lower_corners:
        #         sum_diag_bidang = 0
        #         j_lower = lower_corner[0]
        #         i_lower = lower_corner[1]
                
        #         j_range = range(0,dim) if j_lower == 1 else range(dim-1,-1,-1)
        #         i_range = range(0,dim) if i_lower == 1 else range(dim-1,-1,-1)
                
        #         for j, i in list(zip(j_range, i_range)):
        #             sum_diag_bidang += self._cube.values[i][j][k]
                
        #         if sum_diag_bidang != magic_number:
        #             conflicting += 1 
            
        # return -conflicting
     

        # # Convert values to a numpy array for efficient slicing and summation
        # values = np.array(self._cube.values)

        # # Initialize conflict count
        # conflicting = 0

        # # Check row sums (across the x-axis), column sums (y-axis), and pillar sums (z-axis)
        # row_sums = values.sum(axis=2)
        # col_sums = values.sum(axis=0)
        # pillar_sums = values.sum(axis=1)

        # # Count conflicts for rows, columns, and pillars
        # conflicting += np.sum(row_sums != magic_number)
        # conflicting += np.sum(col_sums != magic_number)
        # conflicting += np.sum(pillar_sums != magic_number)

        # # Space diagonals
        # if np.trace(values, axis1=0, axis2=1).sum() != magic_number:
        #     conflicting += 1
        # if np.trace(values[::-1], axis1=0, axis2=1).sum() != magic_number:
        #     conflicting += 1
        # if np.trace(values[:, ::-1, :]).sum() != magic_number:
        #     conflicting += 1
        # if np.trace(values[:, :, ::-1]).sum() != magic_number:
        #     conflicting += 1

        # # Plane diagonals in xy, yz, and xz planes (forward and reverse)
        # for i in range(dim):
        #     if values[i].diagonal().sum() != magic_number:  # xy-plane
        #         conflicting += 1
        #     if values[:, i, :].diagonal().sum() != magic_number:  # yz-plane
        #         conflicting += 1
        #     if values[:, :, i].diagonal().sum() != magic_number:  # xz-plane
        #         conflicting += 1
        #     if values[i, :, ::-1].diagonal().sum() != magic_number:  # xy-plane, reverse
        #         conflicting += 1
        #     if values[:, i, ::-1].diagonal().sum() != magic_number:  # yz-plane, reverse
        #         conflicting += 1
        #     if values[::-1, :, i].diagonal().sum() != magic_number:  # xz-plane, reverse
        #         conflicting += 1

        # return -conflicting
