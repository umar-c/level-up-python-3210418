from itertools import product

def solve_sudoku_exp(sudoku : list):
  if len(sudoku) != 9:
    print("Not a valid sudoku puzzle! Exiting...")
    return
  
  solved_sudoku = sudoku.copy()

  for row in solved_sudoku:
    idx = 0
    empty_indices = []
    empty_indices_idx = 0
    
    while idx < len(row) and 0 in row[idx:]:
        idx = row.index(0)
        empty_indices.append(idx)

    for n in range(1,10):
      while n not in row:
        idx = empty_indices[empty_indices_idx]
        
        n_in_column = False
        for r in solved_sudoku:
          if r[idx] == n:
            n_in_column = True
            empty_indices_idx += 1 # if idx < len(row) - 1 else idx
            break
        
        if not n_in_column:
          row[idx] = n
          empty_indices.pop(idx)
        elif empty_indices_idx == len(row):
          empty_indices_idx = 0
          # Swap elements
          row[empty_indices[empty_indices_idx]], row[empty_indices[empty_indices_idx+1]] = row[empty_indices[empty_indices_idx+1]], row[empty_indices[empty_indices_idx]]
          empty_indices_idx += 1 if empty_indices_idx < len(empty_indices_idx) - 1 else 0
  
  return solved_sudoku

def solve_sudoku(puzzle):
  for (row, col) in product(range(0, 9), repeat=2):
    if puzzle[row][col] == 0:
      for num in range(1, 10):
        allowed = True
        for i in range(0, 9):
          if num in (puzzle[i][col], puzzle[row][i]):
            allowed = False
            break
        for (i, j) in product(range(0, 3), repeat=2):
          if num == puzzle[row - row % 3 + i][col - col % 3 +j]:
            allowed = False
            break
        if allowed:
          puzzle[row][col] = num
          if trial := solve_sudoku(puzzle):
            return trial
          puzzle[row][col] = 0
      return False
  return puzzle

def print_sudoku_simple(sudoku):
  for row in sudoku:
    print(row)

def print_sudoku(puzzle):
  puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
  print()
  for row in range(0, 9):
    if ((row % 3 == 0) and (row != 0)):
      print('-' * 33)
    for col in range(0, 9):
      if ((col % 3 == 0) and (col != 0)):
        print(' | ', end='')
      print(f' {puzzle[row][col]} ', end='')
    print()
  print()

test_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]

hardest_sudoku = [
                [8,0,0,0,0,0,0,0,0],
                [0,0,3,6,0,0,0,0,0],
                [0,7,0,0,9,0,2,0,0],
                [0,5,0,0,0,7,0,0,0],
                [0,0,0,0,4,5,7,0,0],
                [0,0,0,1,0,0,0,3,0],
                [0,0,1,0,0,0,0,6,8],
                [0,0,8,5,0,0,0,1,0],
                [0,9,0,0,0,0,4,0,0]]

# commands used in solution video for reference
if __name__ == '__main__':
    print_sudoku(test_puzzle)
    # solution = solve_sudoku_exp(test_puzzle)
    solution = solve_sudoku(test_puzzle)
    print('\n')
    print_sudoku(solution)

    print_sudoku(hardest_sudoku)
    solution = solve_sudoku(hardest_sudoku)
    print('\n')
    print_sudoku(solution)