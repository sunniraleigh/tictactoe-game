# A terminal-played tic tac toe game
# Written by @sunniraleigh
# To play: run `python3 ticTacToe.py`

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

# GAMEPLAY

# run game
print("Starting game with" + num_of_players + "players")
running = True

while(running == True):

  # player 1 turn
  # check for player 1 win
    # check if player 2 is person or computer
      # player 2 turn
      # check for player 2 turn
  # check for draw

# GAMEPLAY FUNCTIONS
# player turn, input player, no output, updates board
def player_turn(player):
  active_turn = True

  while(active_turn == True):
    # ask player to enter row and col values
    player_row = input("Select a slot row (0-3):")
    player_col = input("Select a slot column (0-3):")
    
    if check_open_slot(player_row, player_col):
      update_board(player, player_row, player_col)
      active_turn = False

  return

# check for open slot
# check for win
# check for draw
# update board
def update_board(player, player_row, player_col):
  board[player_row, player_col] = player
  return
