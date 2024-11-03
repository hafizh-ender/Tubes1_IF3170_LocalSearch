import numpy as np
import copy
from typing import Optional

class Cube:
    def __init__(self, dim: int = 5, values: Optional[np.ndarray] = None):
        if values is not None:
            self._values: np.ndarray = values
            self._dim: int = values.shape[0]
        else:
            self._values = np.arange(1, dim ** 3 + 1)
            np.random.shuffle(self._values)
            self._values = np.reshape(self._values, (dim, dim, dim))
            self._dim = dim
        
        self._magic_number: float = self._dim * (self._dim ** 3 + 1) / 2

    @property
    def dim(self) -> int:
        return self._dim

    @property
    def magic_number(self) -> float:
        return self._magic_number

    @property
    def values(self) -> np.ndarray:
        return self._values

    @values.setter
    def values(self, new_values: np.ndarray) -> None:
        if new_values.shape == (self._dim, self._dim, self._dim):
            self._values = new_values
        else:
            raise ValueError("Values array dimensions do not match the cube's dimension")