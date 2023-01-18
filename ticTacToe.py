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
      player_row = input("Select a slot row (0-3):")
      player_col = input("Select a slot column (0-3):")
    else:
      # generate random row and col
      player_row = random.randint(3)
      player_col = random.randint(3)
    
    if check_open_slot(player_row, player_col):
      update_board(board, player, player_row, player_col)
      active_turn = False

# check for open slot
def check_open_slot(player_row, player_col):
  return board[player_row, player_col] == 0

# check for win
def check_win(player):
  # how is a win determined
  # 3 horizontal solutions
  # 3 vertical solutions
  # 2 diagonal solutions

# check for draw
# iterate over board and see if there are any 0's left
def check_draw():
  for row in board:
    for col in row:
      if col == 0:
        return False
  return True

# update board
def update_board(board, player, player_row, player_col):
  board[player_row, player_col] = player
  return board

# GAMEPLAY
# run game
print("Starting game with" + num_of_players + "players")
running = True

while(running == True):
  # player 1 turn
  player_turn(1, False)
  # check for player 1 win
  if check_win(1):
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
    running != check_win(2)
  # check for draw
    running != check_draw()