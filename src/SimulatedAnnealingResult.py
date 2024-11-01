from BaseResult import BaseResult
import numpy as np

class SimulatedAnnealingResult(BaseResult):
    def __init__(self):
        super().__init__()
        self._deltaE_history = []
        self._temperature_history = []
        self._exponent_history = []
        
    def add_exponent(self, deltaE, temperature):
        self._deltaE_history.append(deltaE)
        self._temperature_history.append(temperature)
        self._exponent_history.append(min(np.exp(deltaE/temperature),1))

    @property
    def deltaE_history(self):
        return self._deltaE_history
    
    @property
    def temperature_history(self):
        return self._temperature_history
    
    @property
    def exponent_history(self):
        return self._exponent_history
    