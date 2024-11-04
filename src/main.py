from BaseAlgorithm import BaseAlgorithm
from BaseResult import BaseResult
from GeneticAlgorithm import GeneticAlgorithm
from RandomRestartAlgorithm import RandomRestart
from SidewaysMoveAlgorithm import SidewaysMoveAlgorithm
from SimulatedAnnealingAlgorithm import SimulatedAnnealingAlgorithm
from SteepestAscentAlgorithm import SteepestAscentAlgorithm
from StochasticHillClimbingAlgorithm import StochasticHillClimbingAlgorithm

from initial_cubes import cube1, cube2, cube3

from State import State
import time


def main(case: int = None) -> None:
    # Convert each initial cube into a State object
    initial_states = [State(cube=cube1), State(cube=cube2), State(cube=cube3)]

    # Dictionary of algorithms with case numbers
    algorithms = {
        1: ("Genetic Algorithm", GeneticAlgorithm),
        2: ("Random Restart", RandomRestart),
        3: ("Sideways Move", SidewaysMoveAlgorithm),
        4: ("Simulated Annealing", SimulatedAnnealingAlgorithm),
        5: ("Steepest Ascent", SteepestAscentAlgorithm),
        6: ("Stochastic Hill Climbing", StochasticHillClimbingAlgorithm),
    }

    results = []

    # Run the specified algorithm if a valid case is provided
    if case is not None and case in algorithms:
        name, algo_class = algorithms[case]
        print(f"Running {name} on each initial state...")

        for i, initial_state in enumerate(initial_states, start=1):
            start_time = time.time()
            result = algo_class.solve(initial_state) if case != 1 else algo_class.solve([initial_state])
            end_time = time.time()

            # Save result and duration
            result.duration = end_time - start_time
            results.append(result)


            print(f"{name} (Initial State {i})\nDuration: {result.duration:.4f} seconds\nIterations: {result.iteration}")

        return results

    # Run all algorithms if no specific case is provided
    else:
        print("Running all algorithms...")
        for case, (name, algo_class) in algorithms.items():
            for i, initial_state in enumerate(initial_states, start=1):
                start_time = time.time()
                result = algo_class.solve(initial_state) if case != 1 else algo_class.solve([initial_state])
                end_time = time.time()

                # Save result and duration
                result.duration = end_time - start_time
                results.append((name, i, result))


                print(f"{name} (Initial State {i}) Duration: {result.duration:.4f} seconds")

    return results

if __name__ == "__main__":
    results = main(case=5)  # Change case to the desired algorithm number, or None for all algorithms

    # Visualize results
    print(f"\nVisualizing result 1")
    BaseAlgorithm.visualize(result[0])
    BaseAlgorithm.visualize3D_subplots(result[0])

    print(f"\nVisualizing result 2")
    BaseAlgorithm.visualize(result[1])
    BaseAlgorithm.visualize3D_subplots(result[1])

    print(f"\nVisualizing result 3")
    BaseAlgorithm.visualize(result[2])
    BaseAlgorithm.visualize3D_subplots(result[2])
