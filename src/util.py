from State import State
import copy
import random

class Utility:
    @staticmethod
    def getNeighbour(state, coordinate1, coordinate2):
        neighbour_cube = state.cube.__copy__()
        
        value1 = neighbour_cube.values[coordinate1[0], coordinate1[1], coordinate1[2]]
        value2 = neighbour_cube.values[coordinate2[0], coordinate2[1], coordinate2[2]]
        neighbour_cube.values[coordinate1[0], coordinate1[1], coordinate1[2]] = value2
        neighbour_cube.values[coordinate2[0], coordinate2[1], coordinate2[2]] = value1
        
        return State(neighbour_cube)
    
    @staticmethod
    def generateCoordinatePairs(dim):
        coordinates = [[i, j, k] for i in range(dim) for j in range(dim) for k in range(dim)]
        return [(coordinates[i], coordinates[j]) for i in range(len(coordinates)) for j in range(i + 1, len(coordinates))]

    @staticmethod
    def getRandomSuccessor(state):
        coordinate_pairs = Utility.generateCoordinatePairs(state.cube.dim)
        coordinate1, coordinate2 = random.choice(coordinate_pairs)
        
        return Utility.getNeighbour(state, coordinate1, coordinate2)
    
    @staticmethod
    def getBestSuccessor(state):
        best_state = None
        best_value = float('-inf')
        
        coordinate_pairs = Utility.generateCoordinatePairs(state.cube.dim)
        
        for coordinate1, coordinate2 in coordinate_pairs:
            successor_state = Utility.getNeighbour(state, coordinate1, coordinate2)
            
            if successor_state.value > best_value:
                best_value = successor_state.value
                best_state = successor_state
        
        return best_state
