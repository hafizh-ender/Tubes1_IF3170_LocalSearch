from BaseResult import BaseResult
from State import State

from typing import List, Any

class GeneticAlgorithmResult(BaseResult):
    def __init__(self, n_population: int = 4):
        super().__init__()
        self._n_population = n_population
        self._iteration = 0
        self._population_history = []
        self._population_values_history = []
    
    def add_state(self, state: State, population: List[State]) -> None:
        super().add_state(state)
        
        self._population_history.append(population)
        self._population_values_history.append([individual.value for individual in population])

    @property
    def iteration(self) -> int:
        return self._iteration
    
    @property
    def n_population(self) -> int:
        return self._n_population
    
    @iteration.setter
    def iteration(self, value: int) -> None:
        self._iteration = value
        
    @property
    def population_history(self) -> List[List[State]]:
        return self._population_history
    
    @property
    def population_values_history(self) -> List[List[float]]:
        return self._population_values_history