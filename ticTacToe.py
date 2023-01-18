# A terminal-played tic tac toe game
# Written by @sunniraleigh
# To play: run `python3 ticTacToe.py`

# define or clear board
board = [[0,0,0], [0,0,0], [0,0,0]] # 0 is empty slot
# update list of empty slots
empty_slots = [] # initialize list
for row in board:
  for col in row:
    if col == 0:
      empty_slots.append([row,col])
# determine if there is 1 player or 2 players

# GAMEPLAY

# ask if ready to play
# run game

  # player 1 turn
  # check for player 1 win
    # check if player 2 is person or computer
      # player 2 turn
      # check for player 2 turn
  # check for draw

# GAMEPLAY FUNCTIONS
# player turn, input player, no output, updates board
# check for open slot
# check for win
# check for draw
# update board
