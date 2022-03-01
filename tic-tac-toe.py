# Tic Tac Toe
# Yongdong Xi & Jason Diao

# This function is used to created a gameboard by creating a 3 * 3 matrix.
def create_gameboard():
  board = [[0,0,0],[0,0,0],[0,0,0]]

  return board

# This function is used to display the gameboard onto the console by using a for loop to go through each element within the matrix.
# If the element is 0 it means that there is a blank space here, 1 represents marker o, 2 represents marker x.
def display_board(gameboard):
  display = gameboard.copy()
  
  for i1,r in enumerate(gameboard):
    for i2,c in enumerate(r):
      if gameboard[i1][i2] == 0:
        display[i1][i2] = " "
      elif gameboard[i1][i2] == 1:
        display[i1][i2] = "o"
      elif gameboard[i1][i2] == 2:
        display[i1][i2] = "x"
  
  for i,v in enumerate(gameboard):
    if i == 0:
      print("  "+gameboard[0][0]+" | "+gameboard[0][1]+" | "+gameboard[0][2]+"  ")
      print("-------------")
    elif i == 1:
      print("  "+gameboard[1][0]+" | "+gameboard[1][1]+" | "+gameboard[1][2]+"  ")
      print("-------------")
    else:
      print("  "+gameboard[2][0]+" | "+gameboard[2][1]+" | "+gameboard[2][2]+"  ")

# This function is used to place markers onto the gameboard. The parameter i and v are the row and column of the gameboard, the gameboard is the matrix created previously, and the side indicates if marker x or o will be placed onto the gameboard.
def place_marker(i,v,gameboard,side):
      if side == 1:
        gameboard[i][v] = 1
      elif side == 2:
        gameboard[i][v] = 2



# This function is used to keep track of what player it is to place markers in the current round. It is written for convenience, not for necessity.
def check_player(round):
  if round % 2 == 0:
    return 1
  else:
    return 2

# This function is created for checking if the gameboard is filled with markers. It is written for draw game checking.
def isboardfull(board):
    space = 0
    for k in board:
        for v in k:
            if v == " ":
                space += 1
    if space != 0:
      return False
    else:
      return True
      

# This function is for checking if a winner is generated. It is basically a ton of if statements to check for winning condition.
def check_win(board):
  # Rows condition checking
  for x in board:
    if x[0] == x[1] == x[2]:
      if x[0] == 'o':
        return 1
      elif x[0] == 'x':
        return 2
  # Columns condition checking
  y = 0
  check = []
  first = []
  while y < 3:
    for row in board:
      first.append(row[y])
    check.append(first)
    first = []
    y += 1
  if ["o","o","o"] in check:
    return 1
  elif ["x","x","x"] in check:
    return 2
  # Diagonal condition checking
  if board[0][0] == board[1][1] == board[2][2]:
    if board[0][0] == "o":
      return 1
    elif board[0][0] == "x":
      return 2

  if board[0][2] == board[1][1] == board[2][0]:
    if board[1][1] == "o":
      return 1
    elif board[2][2] == "x":
      return 2

  return 0

# We initially thought to add a mode playing against a bot, but there was not enough time for us to do so, so we gave up this idea.
def bot(board):
    blank = [board[1][1], board[0][0], board[2][2], board[0][2], board[2][0], board[0][1], board[1][0], board[1][2], board[2][1]]
    for s in blank:
        if s != '0':
            continue
        elif s == '0':
            return s
        break
        
# This is the main body of the game. It is the combination of all the piece functions that we previously wrote.
# It will generate a gameboard first, then place the marker, check if a grid has been taken, update the gameboard display, check win condition, and enter the next loop by using a while True loop.
def game(counter):
  gameboard = create_gameboard()
  display_board(gameboard)
  player = check_player(counter)
  step = []
  coord = input("Player {0}, please enter the coordinate (x,y): ".format(player))
  place_marker(int(coord[0]),int(coord[2]),gameboard,player)
  counter += 1
  step.append([int(coord[0]),int(coord[2])])
  display_board(gameboard)
  while True:
    player = check_player(counter)
    coord = input("Player {0},lease enter the coordinate (x,y): ".format(player))
    while True:
      if [int(coord[0]),int(coord[2])] not in step:
        step.append([int(coord[0]),int(coord[2])])
        break
      print("This grip has been taken")
      coord = input("Player {0}, enter the coordinate again: ".format(player))
    if player == 1:
        place_marker(int(coord[0]),int(coord[2]),gameboard,1)
        counter += 1
    elif player == 2:
        place_marker(int(coord[0]),int(coord[2]),gameboard,2)
        counter += 1
    display_board(gameboard)
    if check_win(gameboard) != 0:
      print("Player {0} wins".format(check_win(gameboard)))
      if check_win(gameboard) == 1:
        return 1
      elif check_win(gameboard) == 2:
        return 2
    else:
      if isboardfull(gameboard) == True:
        print("Draw!")
        return 0
    
# In order to have a scoreboard and be able to play again, a play game function is created so that it can record the score, run the game() function again, and switch the order of marker placing. The game() function will return 0, representing draw; 1, representing player 1 wins; 2, representing player 2 wins.
def play_game():
  score1 = 0
  score2 = 0
  player = 0
  while True:
    
    play = game(player)
    if play == 1:
      score1 += 1
    elif play == 2:
      score2 += 1
  
    print("Score board\nP1 VS P2\n {0}     {1}".format(score1,score2))

    run = input("Do you want to play another round?(Enter y for yes and n for no): ")
    if run == "y":
      player += 1
      continue
    else:
      break
  
play_game()
