# A terminal-played tic tac toe game
# Written by @sunniraleigh
# To play: run `python3 ticTacToe.py`

import random

# define or clear board
board = [[0,0,0], [0,0,0], [0,0,0]] # 0 is empty slot
# # update list of empty slots
# empty_slots = [] # initialize list
# for row in board:
#   for col in row:
#     if col == 0:
#       empty_slots.append([row,col])
# determine if there is 1 player or 2 players
num_of_players = input("Please indicate how many players there are (1 or 2):")

# GAMEPLAY FUNCTIONS
# player turn, input player, no output, updates board
def player_turn(player, if_comp):
  active_turn = True

  while(active_turn == True):
    if not if_comp:
      # ask player to enter row and col values
      player_row = int(input("Select a slot row (0-3):"))
      player_col = int(input("Select a slot column (0-3):"))
    else:
      # generate random row and col
      player_row = random.randint(0, 3)
      player_col = random.randint(0, 3)
    
    if check_open_slot(player_row, player_col):
      update_board(board, player, player_row, player_col)
      active_turn = False

# check for open slot
def check_open_slot(player_row, player_col):
  return True if board[player_row][player_col] == 0 else False

# check for win
def check_win(player, board):
  return True if random.randint(0, 2) == 1 else False
  # iterate through rows and determine if all values are the same and not 0
  # this is not ideal ripp
  # for row in board:
  #   # check for horizontal win
  #   for col in row:
  #     if board[row][col] == player:
  #       check_next_row = True
  #       # check if there's another slot, dependent on size of board?
  #       if col == 2:
  #         return True # reached the end of a full row therefore a win
  #     else:
  #       check_next_row = False
  #     if check_next_row == False:
  #       break
    
    # check for vertical win
    # for col in row:
    #   if board[row][col] == player:
    #     check_next_col = True


  # how is a win determined
  # 3 horizontal solutions
  # 3 vertical solutions
  # 2 diagonal solutions

# check for draw
# iterate over board and see if there are any 0's left
def check_draw(board):
  for row in board:
    for col in row:
      if col == 0:
        return False
  return True

# update board
def update_board(board, player, player_row, player_col):
  board[player_row][player_col] = player
  return board

# print board
def print_board(board):
  for row in board:
    for col in row:
      print(col)
    print()

# GAMEPLAY
# run game
print("Starting game with" + num_of_players + "players")
running = True

while(running == True):
  print_board(board)
  # player 1 turn
  player_turn(1, False)
  # check for player 1 win
  if check_win(1, board):
    running = False
  else:
    # check if player 2 is person or computer
    if num_of_players == 1:
      # generate computer turn
      player_turn(2, True)
    else:
      # player 2 turn
      player_turn(2, False)
    # check for player 2 win
    running != check_win(2, board)
  # check for draw
    running != check_draw(board)