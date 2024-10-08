# Phoenix Valent
  # U2L3
    # Make Tic-Tac-Toe in Python

import tic_tac_toe as t
from os import system as screen
import random

def checkInput(inp, board): # checks if the input works, loops back if it doesn't
  try:
    intInp = int(inp)
  except:
    input("Please enter a number between one and nine. Press enter to try again.")
    gaming(board)
  return intInp

def botMovin(board): # bot movement system
  choice = random.randint(1, 9)
  board.place_token(choice)
  
def playAgain(): # gives the user the option to play again. not required, but it took like three minutes so it's a net positive
  perchance = input("Would you like to play again? y/n ")
  if perchance.lower() == 'y':
    main()
  elif perchance.lower() == 'n':
    print("Okay, bye!")
  else:
    input("Please enter y for yes or n for no. Press enter to try again.")
    screen("clear")
    playAgain()

def gaming(board): # pretty much just the main function, but I enjoy having a clean main function so I shoved everything in here
  gameOver = False
  while gameOver == False:
    print(board)
    winner, gameOver = board.is_winner()
    if not gameOver:
      if board.check_turn() == "X":
        playerChoice = input("Which tile would you like to place in? ")
        inp = checkInput(playerChoice, board)
        board.place_token(inp)
        print(board)
      elif board.check_turn() == "O":
        botMovin(board)
      winner, gameOver = board.is_winner()
      screen("clear")
  print(board)
  if winner == 'X':
    print("You won!\n\n")
  elif winner == 'O':
    print("The CPU won!\n\n")
  elif winner == 'T':
    print("It's a tie 😔\n\n")
  playAgain()

def intro(): # informs the player how to play and which tile is which
  screen("clear")
  print("To play this Tic-Tac-Toe, simply input a number 1-9 that corresponds to a tile on the game board, like so:\n\n")
  print(f" 1 | 2 | 3 \n{'-'*11}\n 4 | 5 | 6 \n{'-'*11}\n 7 | 8 | 9 \n\n")
  print("Then, the computer will place a tile in a random unused space. You play Xs, the computer plays Os. The game ends when no tiles can be placed, or one player wins by getting three of their letters in a row.")
  input("Press ENTER to begin.")

def main(): # previously mentioned clean main function
  intro()
  gaming(t.TicTacToe())

if __name__ == "__main__": # calls the main function so things actually happen
  main()