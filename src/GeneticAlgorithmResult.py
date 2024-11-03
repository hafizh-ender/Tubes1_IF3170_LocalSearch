from BaseResult import BaseResult
from State import State

from typing import List, Any

# GeneticAlgorithmResult class for storing population history and values
class GeneticAlgorithmResult(BaseResult):
    def __init__(self, n_population: int = 4):
        super().__init__()
        self._n_population = n_population
        self._population_history: List[List[State]] = []
        self._population_values_history: List[List[int]] = []
    
    def add_state(self, state: State, population: List[State]) -> None:
        """Add state and current population values to history."""
        super().add_state(state)
        self._population_history.append(population)
        self._population_values_history.append([ind.value for ind in population])

    @property
    def n_population(self) -> int:
        return self._n_population
        
    @property
    def population_history(self) -> List[List[State]]:
        return self._population_history
    
    @property
    def population_values_history(self) -> List[List[int]]:
        return self._population_values_history
