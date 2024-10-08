import random # imports the random library for use in the self.__turn attribute

class TicTacToe:
  def __init__(self): # initialize the class
    self.__board = [["." for x in range(3)] for y in range(3)]
    self.__turn = random.choice(["X", "O"])

  def __str__(self): # displaying the game board
    return f" {self.__board[0][0]} | {self.__board[0][1]} | {self.__board[0][2]} \n{'-'*11}\n {self.__board[1][0]} | {self.__board[1][1]} | {self.__board[1][2]} \n{'-'*11}\n {self.__board[2][0]} | {self.__board[2][1]} | {self.__board[2][2]} "
  
  def __check__win(self): # checks if a player has won, or if it's a tie
    moves = 0
    combos = [
      [self.__board[0][0], self.__board[0][1], self.__board[0][2]], # top row
      [self.__board[1][0], self.__board[1][1], self.__board[1][2]], # middle row
      [self.__board[2][0], self.__board[2][1], self.__board[2][2]], # bottom row
      [self.__board[0][0], self.__board[1][0], self.__board[2][0]], # left column
      [self.__board[0][1], self.__board[1][1], self.__board[2][1]], # middle column
      [self.__board[0][2], self.__board[1][2], self.__board[2][2]], # right column
      [self.__board[0][0], self.__board[1][1], self.__board[2][2]], # L->R diagonal
      [self.__board[0][2], self.__board[1][1], self.__board[2][0]]  # R->L diagonal
    ]
    for i in combos:
      if i[0] == i[1] == i[2]:
        if i[0] == "X":
          return "X"
        elif i[0] == "O":
          return "O"
    for i in self.__board:
      for j in i:
        if j != ".":
          moves+=1
    if moves == 9:
      return "T"
    return ""


  def place_token(self, inp): # attempts to place a token on the game board. if it doesn't work, the while loop in main just allows it to try again until it gets it right without switching the turn
    works = True

    if inp == 1:
      r = 0 # r for row, c for column
      c = 0 # it just looks cleaner later on I swear I'm not turning into Griffin

    elif inp == 2:
      r = 0
      c = 1

    elif inp == 3:
      r = 0
      c = 2

    elif inp == 4:
      r = 1
      c = 0

    elif inp == 5:
      r = 1
      c = 1

    elif inp == 6:
      r = 1
      c = 2

    elif inp == 7:
      r = 2
      c = 0

    elif inp == 8:
      r = 2
      c = 1

    elif inp == 9:
      r = 2
      c = 2

    else:
      works = False

    if self.__board[r][c] == 'X' or self.__board[r][c] == 'O':
      works = False

    if works == True:

      self.__board[r][c] = self.__turn

      if self.__turn == "X":
        self.__turn = "O"

      elif self.__turn == "O":
        self.__turn = "X"

  def is_winner(self): # accesses the private __check__win() function and interprets the results
    winVal = self.__check__win()
    if winVal != "":
      gameOver = True
    else:
      gameOver = False
    return winVal, gameOver

  def get_board(self): # gets the game board
    return self.__board

  def check_turn(self): # checks whose turn it is
    return self.__turn