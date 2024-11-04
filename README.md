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
You can run one of the demo files `main.py` [arvi ngisi]

### Video Player
[fadli ngisi]