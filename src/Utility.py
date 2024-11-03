import random
import copy
from State import State
import numpy as np


class Utility:

    @staticmethod
    def is_row_constraint_violated(state: State, p: list[int]) -> bool:
        [f, r, _] = p

        return np.sum(state.cube[f][r]) != Utility.get_magic_number(state.cube.shape[0])

    @staticmethod
    def is_column_constraint_violated(state: State, p: list[int]) -> bool:
        [f, _, c] = p

        return np.sum(state.cube[f, :, c]) != Utility.get_magic_number(state.cube.shape[0])

    @staticmethod
    def get_magic_number(n: int) -> int:
        return (n * (n ** 3 + 1)) / 2

    @staticmethod
    def get_objective_value(state: State) -> int:
        n = state.cube.shape[0]
        magic_number = Utility.get_magic_number(n)

        pillars = [[0] * n for _ in range(n)]

        conflict = 0

        for frame in state.cube:
            # row
            conflict += np.count_nonzero(np.sum(frame, axis=1) != magic_number)

            # column
            conflict += np.count_nonzero(np.sum(frame, axis=0) != magic_number)

            # diagonal
            conflict += np.sum(np.diagonal(frame)) != magic_number
            conflict += np.sum(np.fliplr(frame).diagonal()) != magic_number

            # pillars
            pillars += frame

        conflict += np.sum(pillars != magic_number)

        diagonals = np.zeros(4, dtype=int)
        for i in range(n):
            diagonals[0] += state.cube[i][i][i]
            diagonals[1] += state.cube[i][i][n - 1 - i]
            diagonals[2] += state.cube[i][n - 1 - i][i]
            diagonals[3] += state.cube[i][n - 1 - i][n - 1 - i]
        conflict += np.count_nonzero(diagonals != magic_number)

        for i in range(n):
            conflict += np.sum(state.cube[range(n), range(n), i]) != magic_number
            conflict += np.sum(state.cube[range(n), n - 1 - np.arange(n), i]) != magic_number

        for i in range(n):
            conflict += np.sum(state.cube[range(n), i, range(n)]) != magic_number
            conflict += np.sum(state.cube[range(n), i, n - 1 - np.arange(n)]) != magic_number

        return -conflict

    @staticmethod
    def should_continue(state: State, p1: list[int]) -> bool:
        count_not_violated = 0

        if (
                not Utility.is_row_constraint_violated(state, p1)
        ):
            count_not_violated += 1

        if (
                not Utility.is_column_constraint_violated(state, p1)
        ):
            count_not_violated += 1

        return count_not_violated == 0

    @staticmethod
    def initialize_state(n: int) -> State:
        elements = np.arange(1, n ** 3 + 1)

        np.random.shuffle(elements)

        cube = elements.reshape((n, n, n))

        return State(cube)

    @staticmethod
    def get_random_successor(state: State) -> State:
        m = len(state.cube) - 1

        while True:
            first = np.random.randint(0, m + 1, size=3)
            second = np.random.randint(0, m + 1, size=3)

            if not np.array_equal(first, second):
                if not Utility.should_continue(state, first):
                    continue

                cube = np.copy(state.cube)
                cube[tuple(first)], cube[tuple(second)] = cube[tuple(second)], cube[tuple(first)]

                return State(cube)

    @staticmethod
    def get_best_successor(state: State) -> State:
        n = state.cube.shape[0]
        best_neighbors = []
        best_objective_value = float('-inf')

        positions = [(f, r, c) for f in range(n) for r in range(n) for c in range(n)]

        for p1 in positions:
            for p2 in positions:
                if p1 == p2:
                    continue
                if not Utility.should_continue(state, p1):
                    continue

                successor = copy.deepcopy(state)
                successor.swap_position(p1, p2)

                if successor.objective_value > best_objective_value:
                    best_neighbors = [successor]
                    best_objective_value = successor.objective_value
                elif successor.objective_value == best_objective_value:
                    best_neighbors.append(successor)

        return best_neighbors[random.randint(0, len(best_neighbors) - 1)]
