# Sudoku Solver in Python

## Overview
This project is a backtracking-based Sudoku solver implemented in Python. It takes an incomplete Sudoku board (9×9 grid) as input and attempts to fill in the missing values while following Sudoku rules:

- Each row must contain numbers from 1 to 9 without repetition.  
- Each column must contain numbers from 1 to 9 without repetition.  
- Each of the nine 3×3 subgrids must contain numbers from 1 to 9 without repetition.  

The algorithm systematically tests possible numbers for each empty cell and backtracks when a contradiction occurs.

---

## Features
- Validates moves according to Sudoku constraints.  
- Uses a recursive backtracking algorithm for solving.  
- Example Sudoku board included for testing.  
- Can be easily extended to accept user input or generate random puzzles.  

---

## Requirements
- Python 3.7+  
(No additional libraries are required.)

---

## Installation
Clone the repository:
```bash
git clone https://github.com/your-username/sudoku-solver.git
cd sudoku-solver
```

Run the script:
```bash
python sudoku_solver.py
```

---

## Usage
The Sudoku board is defined as a 9×9 list of lists in the script.  
Empty cells are represented with `0`.

Example board:
```python
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
```

To solve the board, call:
```python
solve(board, 0, 0)
```

---

## Functions

### `is_valid_move(grid, row, col, number)`
- Checks if a number can be placed in a given cell without violating Sudoku rules.  
- Returns `True` if the move is valid, otherwise `False`.

### `solve(grid, row, col)`
- Attempts to solve the Sudoku puzzle using recursion and backtracking.  
- Returns `True` if the Sudoku is solved, otherwise `False`.
