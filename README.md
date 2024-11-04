# Local Search for Diagonal Magic Cube Problem
This repository serves as the first major assignment of IF3170 Artificial Intelligence course of Informatics Engineering in Institut Teknologi Bandung.

## Table of Contents
 1. [General Information](#general-information)
 2. [Setup](#setup)
 3. [How to Run](#how-to-run)


## General Information
A diagonal magic cube or 'perfect' ,magic cube is a cube  of order $n$ where each side has a length of $n$ and contains unique integers from 1 to $n^3$ and has the sum of $n$ numbers along any straight lines (rows, columns, pillars, diagonals, triagonals) equals to the magic constant:

$M_3 (n) = \frac{n \left(n^3 + 1 \right)}{2}$

A 'perfect' magic cube only exist when $n >= 5$.

In this repository, various local search algorithms will be implemented to solve diagonal magic cube problems. The purpose is mainly to compare the performance of each local search algorithm and to see the viability of each local search algorithm in solving the problem.

## Setup
1. Clone the repository
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/hafizh-ender/Tubes1_IF3170_LocalSearch.git
   ```

2. Navigate to the project directory
   Change into the repository's folder:
   ```bash
   cd Tubes1_IF3170_LocalSearch
   ```

3. Create a virtual environment
   To ensure package compatibility, set up a local environment. For example, using `venv`:
   ```bash
   python -m venv myenv
   ```

4. Activate the virtual environment  
   - On **Windows**:
     ```bash
     .\myenv\Scripts\activate
     ```

5. Install dependencies
   Use `pip` to install the required packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the application**  
   You're now ready to use the repository!

## How to Run
### Demo File
You can run one of the demo files `main.py`, or follow the following basic steps:

1. Import `State`, `BaseAlgorithm`, and your wanted-local-search algorithm (example: `SteepestAscentAlgorithm` for steepest-ascent hill climbing) to your Python file.
2. Initialize a `State` object by specifying the dimension
    ```py
    start_state = State(dim=5)
    ```
    or by having a 3D `numpy.npdarray`
    ```py
    start_state = State(cube=numpy_array)
    ```
3. For genetic algorithm, you have to initiate few states and combine them into a list of states.
    ```py
    start_population = [State(dim=5), State(dim=5), State(dim=5), State(dim=5)]
    ```
4. Run the static method `solve` of the algorithm. For example:
    ```py
    steepest_ascent_hill_climbing_result = SteepestAscentAlgorithm.solve(initial_state=start_state,verbose=True)
    ```
    ```py
    genetic_algorithm_result = GeneticAlgorithm.solve(initial_states=start_population, iteration_max=100000)
    ```
5. Print the result based on the class properties.
6. For visualization, you can use the following:
    ```py
    BaseAlgorithm.visualize(steepest_ascent_hill_climbing_result)
    BaseAlgorithm.visualize3D_subplots(steepest_ascent_hill_climbing_result)
    ```

### Video Player
1. Create an instance of "VideoPlayer"
2. Set up the UI to show the UI
3. Import the corresponding .txt file containing the experiment result
4. Toggle the play/pause button if needed
5. Adjust the playback speed according to your preference
6. Adjust the progress if needed
7. Adjust the view of the cube to switch between different view orientations

You can run the demo file video_player_demo.py