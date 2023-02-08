# A terminal-played tic tac toe game
# Written by @sunniraleigh
# To play: run `python3 ticTacToe.py`

# GAMEPLAY FUNCTIONS

# create a board
def create_board(n):
  board = []

  for i in range(n):
    row = []
    for col in range(n):
      row.append("-")
    board.append(row)

  return board

# check for open slot
def check_open_slot(board, player_row, player_col):
  return True if board[player_row][player_col] == "-" else False

# check for win
# return wins are important because they stop the execution 
# of the rest of the function if there is a win
def check_win(player, board):

  size = len(board)
  win = None

  # check horizontal
  for row in range(size):
    win = True # this is keeping info from previous loop through where it didn't break
    for col in range(size):
      if board[row][col] != player:
        win = False
        break
  if win:
    return win

  # check vertical
  for row in range(size):
    win = True
    for col in range(size):
      if board[col][row] != player:
        win = False
        break
  if win:
    return win

  # check diagonals

  # diagonal across and down
  win = True
  for i in range(size):
    if board[i][i] != player:
      win = False
      break

  if win:
    return win

  # diagonal across and up
  win = True
  for i in range(size):
    if board[i][size - 1 - i] != player:
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
      if col == "-":
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

# player turn, input player, no output, updates board
def player_turn(board, player):
  size = len(board) - 1

  active_turn = True

  print("Player", player, "turn: ")

  while(active_turn == True):

    # select slot
    slot_chosen = False
    # make sure slot coords are correctly entered - only contain 2 values
    while(slot_chosen == False):
      slot_coords = input("Enter coords of selected slot (ex: 0 2):").replace(" ", "")
      player_row = int(slot_coords[0])
      player_col = int(slot_coords[1])
      if player_row > size or player_col > size:
        print("Please enter coordinates w/ values less than or equal to", str(size))
      elif player_row < 0 or player_col < 0:
        print("Please enter coordinates greater than 0")
      elif len(slot_coords) != 2:
        print("Please enter coordinates in the correct format")
      else:
        slot_chosen = True
    
    if check_open_slot(board, player_row, player_col):
      update_board(board, player, player_row, player_col)
      active_turn = False
    else:
      print("That slot is full. Choose a new one.")

# GAMEPLAY

# define or clear board
# board = [["-","-","-"], ["-","-","-"], ["-","-","-"]] # - is empty slot
size_chosen = False
while(size_chosen == False):
  board_size = int(input("Choose a board between size 3 and 10"))
  if board_size >= 3 and board_size <= 10:
    size_chosen = True

board = create_board(board_size)

# run game
running = True

while(running == True):
  print_board(board)
  
  # player 1 turn
  player_turn(board, 1)
  print_board(board)
  # check for player 1 win
  if check_win(1, board):
    print("Player 1 wins")
    print_board(board)
    running = False
  else:
    # player 2 turn
    player_turn(board, 2)
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

    