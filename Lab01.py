# student name: Liam Foster
# student number: 40199382

# A command-line Tic-Tac-Toe game 
import random
from shutil import move

board = [' '] * 9 # A list of 9 strings, one for each cell, 
                  # will contain ' ' or 'X' or 'O'
played = set()    # A set to keep track of the played cells 

def init() -> None:
    """ prints the banner messages 
        and prints the intial board on the screen
    """
    print("Welcome to Tic-Tac-Toe!")
    print("You play X (first move) and computer plays O.")
    print("Computer plays randomly, not strategically.")
    printBoard()

def printBoard() -> None:
    """ prints the board on the screen based on the values in the board list """
    print("\n   "+board[0] + " | " + board[1] + " | " + board[2] + "    0 | 1 | 2")
    print("   --+---+--    --+---+--")
    print("   "+board[3] + " | " + board[4] + " | " + board[5] + "    3 | 4 | 5")
    print("   --+---+--    --+---+--")
    print("   "+board[6] + " | " + board[7] + " | " + board[8] + "    6 | 7 | 8\n")



def playerNextMove() -> None:
    """ prompts the player for a valid cell number, 
        and prints the info and the updated board;
        error checks that the input is a valid cell number 
    """
    # Gets input from player
    move = input("Next move for X (state a valid cell num): ")
    # Checks if input is an integer
    if not move.isdigit():
        print("Must be an integer")
        playerNextMove()
    else:
        # Casts int type to input
        move = int(move)
        # Checks if input is outside bounds or already played
        if move > 8 or move < 0 or move in played:
            print("Must enter a valid cell number")
            playerNextMove()
        else:
            board[move] = 'X'
            played.add(move)
            txt = "You chose cell {}"
            print(txt.format(move))
            printBoard()


def computerNextMove() -> None:
    """ Computer randomly chooses a valid cell, 
        and prints the info and the updated board 
    """
    move = random.randint(0,8)
    # Loops until an unplayed integer is randomly selected
    while move in played:
        move = random.randint(0,8)
    board[move] = 'O'
    played.add(move)
    txt = "Computer chose cell {}"
    print(txt.format(move))
    printBoard()


def hasWon(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
    # Statements check each possible win scenario to see if "who" won
    if board[0] == who and board[1] == who and board[2] == who: return True 
    elif board[3] == who and board[4] == who and board [5] == who: return True
    elif board[6] == who and board[7] == who and board [8] == who: return True
    elif board[0] == who and board[3] == who and board [6] == who: return True
    elif board[1] == who and board[4] == who and board [7] == who: return True
    elif board[2] == who and board[5] == who and board [8] == who: return True
    elif board[0] == who and board[4] == who and board [8] == who: return True
    elif board[2] == who and board[4] == who and board [6] == who: return True
    else: return False

def terminate(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
        it also prints the final messages:
                "You won! Thanks for playing." or 
                "You lost! Thanks for playing." or 
                "A draw! Thanks for playing."  
    """
    # Checks if "who" has won first
    if hasWon(who):
        # Checks if "who" is the player
        if (who == 'X'):
            print("You won! Thanks for playing.")
        else:
            print("You lost! Thanks for playing")
        return True
    # Checks if the board is full
    elif len(played) == 9:
        print("A draw! Thanks for playing.")
        return True
    else:
        return False


if __name__ == "__main__":
    # Use as is. 
    init()
    while True:
        playerNextMove()            # X starts first
        if(terminate('X')): break   # if X won or a draw, print message and terminate
        computerNextMove()          # computer plays O
        if(terminate('O')): break   # if O won or a draw, print message and terminate