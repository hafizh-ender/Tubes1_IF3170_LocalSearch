import matplotlib.pyplot as plt
from BaseResult import BaseResult
class BaseAlgorithm:
    @staticmethod
    def visualize(result: BaseResult) -> None:
        #Objective function plotting
        x = range(1, len(result.objective_function_history) + 1)
        plt.plot(x, result.objective_function_history)
        plt.xlabel('Iteration')
        plt.ylabel('Objective Function Result')
        plt.title('Objective Function Plot at Every Iteration')
        plt.grid(True)
        plt.show()
