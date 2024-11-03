import random
from typing import List, Tuple

from State import State

class Utility:
    @staticmethod
    def getNeighbour(state: State, coordinate1: List[int], coordinate2: List[int]) -> State:
        neighbour_cube = state.cube.__copy__()
        
        value1 = neighbour_cube.values[coordinate1[0], coordinate1[1], coordinate1[2]]
        value2 = neighbour_cube.values[coordinate2[0], coordinate2[1], coordinate2[2]]
        neighbour_cube.values[coordinate1[0], coordinate1[1], coordinate1[2]] = value2
        neighbour_cube.values[coordinate2[0], coordinate2[1], coordinate2[2]] = value1
        
        return State(neighbour_cube)
    
    @staticmethod
    def generateCoordinatePairs(dim: int) -> List[Tuple[List[int], List[int]]]:
        coordinates = [[i, j, k] for i in range(dim) for j in range(dim) for k in range(dim)]
        return [(coordinates[i], coordinates[j]) for i in range(len(coordinates)) for j in range(i + 1, len(coordinates))]

    @staticmethod
    def getRandomSuccessor(state: State) -> State:
        coordinate_pairs = Utility.generateCoordinatePairs(state.cube.dim)
        coordinate1, coordinate2 = random.choice(coordinate_pairs)
        
        return Utility.getNeighbour(state, coordinate1, coordinate2)
    
    @staticmethod
    def getBestSuccessor(state: State) -> State:
        coordinate_pairs = Utility.generateCoordinatePairs(state.cube.dim)
        best_state = max((Utility.getNeighbour(state, coord1, coord2) for coord1, coord2 in coordinate_pairs))
        
        return best_state
