# find an empty grid cell
def find_empty(puzzle): 
  for r in range(9): 
    for c in range(9):
      if puzzle[r][c] == 0:
        return r, c
  return None, None

def is_valid(puzzle, num, row, col): 
  if num in puzzle[row]: 
    return False

  for r in range(9):
     if puzzle[r][col] == num: 
      return False

  row_st = (row // 3) * 3
  col_st = (col // 3) * 3

  for r in range(row_st, row_st + 3): 
    for c in range(col_st, col_st + 3): 
      if puzzle[r][c] == num: 
        return False

  return True



# solve the puzzle
def solve(puzzle): 
  row, col = find_empty(puzzle)
  if row is None: 
    return True

  for num in range(1, 10): 
    if is_valid(puzzle, num, row, col): 
      puzzle[row][col] = num

      if solve(puzzle): 
        return True

      puzzle[row][col] = 0
  return False



##################################################
puzzle = [
          [5, 4, 7, 0, 0, 0, 0, 0, 0], 
          [3, 6, 9, 0, 0, 0, 0, 0, 0], 
          [1, 8, 2, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 9, 2, 3, 0, 0, 0], 
          [0, 0, 0, 8, 1, 4, 0, 0, 0], 
          [0, 0, 0, 6, 7, 5, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 3, 8, 6], 
          [0, 0, 0, 0, 0, 0, 7, 1, 2], 
          [0, 0, 0, 0, 0, 0, 4, 5, 9]]

solve(puzzle)

# output matrix
for r in range(9): 
  for c in range(9):
    print(puzzle[r][c], end = ' ')
  print()

