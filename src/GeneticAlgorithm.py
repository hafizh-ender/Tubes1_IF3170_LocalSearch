import numpy as np
from datetime import datetime
from typing import List, Tuple

from BaseAlgorithm import BaseAlgorithm
from GeneticAlgorithmResult import GeneticAlgorithmResult

from Utility import Utility
from State import State
from Cube import Cube

class Individual:
    def __init__(self, state: State):
        self._state = state
        self._max_fitness_value = 3 * self._state.dim ** 2 + 6 * self._state.dim + 4
        self._fitness_value = self._max_fitness_value + self._state.value

    def __lt__(self, other):
        return self._fitness_value < other._fitness_value

    def __le__(self, other):
        return self._fitness_value <= other._fitness_value

    def __eq__(self, other):
        return self._fitness_value == other._fitness_value

    def __ne__(self, other):
        return self._fitness_value != other._fitness_value

    def __gt__(self, other):
        return self._fitness_value > other._fitness_value

    def __ge__(self, other):
        return self._fitness_value >= other._fitness_value

    @property
    def state(self):
        return self._state
    
    @property
    def fitness_value(self) -> int:
        return self._fitness_value
    
    def is_fitness_value_maximum(self) -> bool:
        return self._fitness_value == self._max_fitness_value

class GeneticAlgorithm(BaseAlgorithm):
    @staticmethod
    def solve(initial_states: List[State], iteration_max: int = 1000, verbose: bool = False) -> GeneticAlgorithmResult:
        start_time = datetime.now()
        
        current_population = [Individual(state=state) for state in initial_states]
        
        n_population = len(initial_states)
        result = GeneticAlgorithmResult(n_population=n_population)
        
        for iteration in range(iteration_max):
            current_population.sort(reverse=True)
            fittest_individual = current_population[0]
            if verbose:
                print(f"Iteration: {iteration}. Value: {fittest_individual.state.value}")
            
            result.add_state(state=fittest_individual.state, population=[individual.state for individual in current_population])
            
            if fittest_individual.is_fitness_value_maximum():
                result.iteration = iteration
                return result
            
            # Generate new population
            new_population = []
            for _ in range(n_population // 2):
                parent1 = GeneticAlgorithm.chooseParent(current_population)
                parent2 = GeneticAlgorithm.chooseParent(current_population)
                
                child1_string, child2_string = GeneticAlgorithm.crossoverPartiallyMapped(
                    parent1.state.cube.ravel(), parent2.state.cube.ravel()
                )
                
                if np.random.rand() > 0.1:
                    child1_string = GeneticAlgorithm.mutateSwap(child1_string)
                if np.random.rand() > 0.1:
                    child2_string = GeneticAlgorithm.mutateSwap(child2_string)
                
                new_population.extend([
                    Individual(state=State(cube=child1_string.reshape(5, 5, 5))),
                    Individual(state=State(cube=child2_string.reshape(5, 5, 5)))
                ])
            
            # if new_population[0].fitness_value > current_population[0].fitness_value:
            current_population = new_population
        
        result.iteration = iteration
        return result

    @staticmethod
    def chooseParent(population: List[Individual]) -> Individual:
        total_fitness = sum(individual.fitness_value for individual in population)
        
        choosen_fitness = np.random.rand() * total_fitness
        
        cumulative_fitness = 0
        for individual in population:
            cumulative_fitness += individual.fitness_value
            if cumulative_fitness >= choosen_fitness:
                return individual
    
    @staticmethod
    def crossoverPartiallyMapped(parent1_string: np.ndarray, parent2_string: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        string_size = len(parent1_string)
        left_crossover_point, right_crossover_point = sorted(np.random.randint(0, string_size, 2))
        child1, child2 = parent1_string.copy(), parent2_string.copy()
        
        child1[left_crossover_point:right_crossover_point], child2[left_crossover_point:right_crossover_point] = parent2_string[left_crossover_point:right_crossover_point], parent1_string[left_crossover_point:right_crossover_point]
        
        mapping1, mapping2 = child1[left_crossover_point:right_crossover_point], child2[left_crossover_point:right_crossover_point]
        for i in range(string_size):
            if i < left_crossover_point or i >= right_crossover_point:
                while child1[i] in mapping1:
                    child1[i] = mapping2[np.where(mapping1 == child1[i])[0][0]]
                while child2[i] in mapping2:
                    child2[i] = mapping1[np.where(mapping2 == child2[i])[0][0]]
        
        return child1, child2

    @staticmethod
    def mutateSwap(individual: np.ndarray) -> np.ndarray:
        idx1, idx2 = np.random.choice(len(individual), 2, replace=False)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
        
        return individual