# Implementation 100% based on Geeksforgeeks post:
# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/

import math


BOARD_SIZE = 3
player, opponent = 'x', 'o'


def print_board(board: list[list[int]]):
  for i in range(BOARD_SIZE):
    print('-------------------')
    print('|     |     |     |')
    print('| ', board[i][0], ' | ', board[i][1], ' | ', board[i][2], ' |')
    print('|     |     |     |')
  print('-------------------')


def is_move_available(board: list[list[int]]):
  for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
      if board[i][j] == '-':
        return True
  return False


def board_score(board: list[list[int]]):
  for i in range(BOARD_SIZE):
    # Find winning rows.
    if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
      if board[i][0] == player:
        return 10
      elif board[i][0] == opponent:
        return -10

    # Find winning columns.
    if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
      if board[0][i] == player:
        return 10
      elif board[0][i] == opponent:
        return -10

  # Find winning diagonals.
  if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    if board[0][0] == player:
      return 10
    elif board[0][0] == opponent:
      return -10

  if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
    if board[0][2] == player:
      return 10
    elif board[0][2] == opponent:
      return -10

  return 0


def minimax(board: list[list[int]], is_max_turn: bool):
  best = board_score(board)
  if best:
    return best
  if not is_move_available(board):
    return 0

  token = player if is_max_turn else opponent
  comp = max if is_max_turn else min
  for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
      if board[i][j] == '-':
        board[i][j] = token
        best = comp(best, minimax(board, not is_max_turn))
        board[i][j] = '-'
  return best


def best_move(board: list[list[int]]):
  best = math.inf
  best_move = (-1, -1)
  for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
      if board[i][j] == '-':
        board[i][j] = opponent
        move = minimax(board, True)
        board[i][j] = '-'
        if move < best:
          best = move
          best_move = (i, j)
  return best_move


def main():
  board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
  ]
  while is_move_available(board) and board_score(board) == 0:
    print_board(board)
    print('\n- Input your next move -')
    i, j = int(input('row [0, 2]: ')), int(input('col [0, 2]: '))
    if (board[i][j] == '-'):
      board[i][j] = player
      if (not board_score(board)):
        opponent_move = best_move(board)
        board[opponent_move[0]][opponent_move[1]] = opponent
  print_board(board)
  score = board_score(board)
  if (score > 0):
    print('\nYou have won!')
  elif (score < 0):
    print('\nThe opponent has won!')
  else:
    print('\nThere has been a tie!')

if __name__ == '__main__':
  main()
