# A terminal-played tic tac toe game
# Written by @sunniraleigh
# To play: run `python3 ticTacToe.py`

# GAMEPLAY FUNCTIONS

# check for open slot
def check_open_slot(board, player_row, player_col):
  return True if board[player_row][player_col] == 0 else False

# check for win
# return wins are important because they stop the execution 
# of the rest of the function if there is a win
def check_win(player, board):

  n = len(board)
  win = None

  # check horizontal
  for row in range(n):
    win = True # this is keeping info from previous loop through where it didn't break
    for col in range(n):
      if board[row][col] != player:
        win = False
        break
  if win:
    return win

  # check vertical
  for row in range(n):
    win = True
    for col in range(n):
      if board[col][row] != player:
        win = False
        break
  if win:
    return win

  # check diagonals

  # diagonal across and down
  win = True
  for i in range(n):
    if board[i][i] != player:
      win = False
      break

  if win:
    return win

  # diagonal across and up
  win = True
  for i in range(n):
    if board[i][n - 1 - i] != player:
      win = False
      break

  if win:
    return win

  return False

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

# print board
def print_board(board):
  
  # get size of board (for scalability!! and assumes that a board is N x N)
  size = len(board)

  # print slot coords for cols
  print("  ", end="")
  for i in range(size):
    print(i, end=" ")
  print()

  # print board and include slot coords for rows
  for row in range(size):
    print(row, end=" ")
    for col in range(size):
      print(board[row][col], end=" ")
    print()

  # print("  1 2 3")
  # for row in board:
  #   print(row, end=" ")
  #   for col in row:
  #     print(col, end=" ")
  #   print()

# player turn, input player, no output, updates board
def player_turn(board, player, if_comp):
  active_turn = True

  print("Player", player, "turn: ")

  while(active_turn == True):
    if not if_comp:
      # ask player to enter row and col values
      player_row = int(input("Select a slot row (0-2):"))
      player_col = int(input("Select a slot column (0-2):"))
    else:
      # generate random row and col
      player_row = random.randint(0, 3)
      player_col = random.randint(0, 3)
    
    if check_open_slot(board, player_row, player_col):
      update_board(board, player, player_row, player_col)
      active_turn = False
    else:
      print("That slot is full. Choose a new one.")

# GAMEPLAY

# define or clear board
board = [[0,0,0], [0,0,0], [0,0,0]] # 0 is empty slot

# determine if there is 1 player or 2 players
num_of_players = input("Please indicate how many players there are (1 or 2):")

# run game
print("Starting game with " + num_of_players + " players")
running = True

while(running == True):
  print_board(board)
  # player 1 turn
  player_turn(board, 1, False)
  print_board(board)
  # check for player 1 win
  if check_win(1, board):
    print("Player 1 wins")
    print_board(board)
    running = False
  else:
    # check if player 2 is person or computer
    if num_of_players == 1:
      # generate computer turn
      player_turn(board, 2, True)
    else:
      # player 2 turn
      player_turn(board, 2, False)

  # check for player 2 win
  if check_win(2, board):
    print("Player 2 wins")
    print_board(board)
    running = False
  
  # check for draw
  if check_draw(board):
    print("Tie game.")
    print_board(board)
    running = False

    