from BaseAlgorithm import BaseAlgorithm
from Utility import Utility
from State import State

from SimulatedAnnealingResult import SimulatedAnnealingResult

import numpy as np
from datetime import datetime

class SimulatedAnnealingAlgorithm(BaseAlgorithm):
    @staticmethod
    def solve(initial_state: State, initial_temperature: float = 100.0, method: str = "linear", threshold: float = 0.5, verbose: bool = False) -> SimulatedAnnealingResult:
        start_time = datetime.now()
        
        current_state = initial_state
        result = SimulatedAnnealingResult()
        
        iteration = 0
        
        while True:
            if verbose:
                print(f"Iteration: {iteration}. Value: {current_state.value}")
            
            result.add_state(state=current_state)
            
            temperature = SimulatedAnnealingAlgorithm.schedule(initial_temperature=initial_temperature, iter=iteration, method=method)
            if abs(temperature) < 1e-10:
                duration = datetime.now() - start_time
                result.duration = duration.total_seconds()
                
                return result
            
            neighbour_state = Utility.getRandomSuccessor(current_state)
            deltaE = neighbour_state.value - current_state.value
            
            result.add_exponent(deltaE=deltaE, temperature=temperature)
            
            if deltaE > 0:
                current_state = neighbour_state
            else:
                if np.exp(deltaE / temperature) > threshold:
                    current_state = neighbour_state
            
            iteration += 1
            
    @staticmethod
    def schedule(initial_temperature: float, iter: int, method: str = "linear") -> float:
        constant = 0.9
        if method == "linear":
            temperature = max(initial_temperature - constant * iter, 0)
        elif method == "exponent":
            temperature = initial_temperature * constant**iter
        else:
            raise ValueError(f"Unknown scheduling method: {method}")
        
        return temperature
