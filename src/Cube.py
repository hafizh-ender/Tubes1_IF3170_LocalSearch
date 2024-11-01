import numpy as np
import copy

class Cube():
    def __init__(self, dim=5, values=None):
        if values is not None:
            self._values = values
            self._dim = values.shape[0]
        else:
            self._values = np.random.choice(range(1, dim**3 + 1), size=(dim, dim, dim))
            self._dim = dim
        
        self._magic_number = self._dim * (self._dim**3 + 1) / 2

    @property
    def dim(self):
        return self._dim

    @property
    def magic_number(self):
        return self._magic_number

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, new_values):
        if new_values.shape == (self._dim, self._dim, self._dim):
            self._values = new_values
        else:
            raise ValueError("Values array dimensions do not match the cube's dimension")

    def __copy__(self):
        new_copy = Cube(values=self._values.copy())
        return new_copy

    def __len__(self):
        return self._dim ** 3

    def __str__(self):
        return f"{self._values}"