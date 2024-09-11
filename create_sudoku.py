import random

import time ## remove later


class Sudoku: 
  def __init__(self): 
    self.board = [[0 for _ in range(9)] for _ in range(9)]


  def print_board(self): 
    for row in range(9): 
      for col in range(9):
        print(self.board[row][col], end = ' ')
      print()


  def initialize_puzzle(self):
    seed = []

    for _ in range(3):
      num_list = list(range(1, 10)) 
      random.shuffle(num_list)
      seed.append(num_list)

    for num in range(9): 
      self.board[(num // 3) + 0][(num % 3) + 0] = seed[0][num]
      self.board[(num // 3) + 3][(num % 3) + 3] = seed[1][num]
      self.board[(num // 3) + 6][(num % 3) + 6] = seed[2][num]


  def find_empty_cell(self): 
    for row in range(9): 
      for col in range(9):
        if self.board[row][col] == 0:
          return row, col
    return None, None


  def is_valid(self, num, row, col): 
    if num in self.board[row]: 
      return False

    for r in range(9):
       if self.board[r][col] == num: 
        return False

    row_st = (row // 3) * 3
    col_st = (col // 3) * 3

    for r in range(row_st, row_st + 3): 
      for c in range(col_st, col_st + 3): 
        if self.board[r][c] == num: 
          return False

    return True


  def solve_puzzle(self): 
    row, col = self.find_empty_cell()
    if row is None: 
      return True

    for num in range(1, 10): 
      if self.is_valid(num, row, col): 
        self.board[row][col] = num
        if self.solve_puzzle(): 
          return True
        self.board[row][col] = 0
    return False


def main(): 
  obj = Sudoku()
  obj.initialize_puzzle()
  obj.solve_puzzle()
  obj.print_board()

if __name__ == "__main__": 
  main()