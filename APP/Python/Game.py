from GameBoard import GameBoard
from PlayerInterface import CLI
from Difficulty import getDifficultyStats
from Actions import PlayerInput
import time,re,sys

winString = r'''
__   __                     _       _ _  
\ \ / /                    (_)     | | | 
 \ V /___  _   _  __      ___ _ __ | | | 
  \ // _ \| | | | \ \ /\ / / | '_ \| | | 
  | | (_) | |_| |  \ V  V /| | | | |_|_| 
  \_/\___/ \__,_|   \_/\_/ |_|_| |_(_|_) 
                                         
                                         
            '''


loseString = r'''
______                       _ _ 
| ___ \                     | | |
| |_/ / ___   ___  _ __ ___ | | |
| ___ \/ _ \ / _ \| '_ ` _ \| | |
| |_/ / (_) | (_) | | | | | |_|_|
\____/ \___/ \___/|_| |_| |_(_|_)
                                 
                                 
            '''

def main():
    difficulty = 1
    gameBoard, gameBoardState = GameBoard.CreateBoards(difficulty)
    MinesFound = {"count": 0}
    print("begin")
    TimeStart = time.time()
    ended = False
    while(True):
        print("\n\n\n\n")
        timeStamp= time.time() - TimeStart
        CLI.ShowGameState(gameBoard,difficulty,MinesFound,timeStamp)
        returnParameter = PlayerInput.Take_command_cli(gameBoard,gameBoardState,MinesFound,difficulty)
        if returnParameter == "Success":
            CLI.PrintBoard(gameBoardState)
            print(f"\n\n\n {winString} \n")
            print(f"Your time: {timeStamp}")
            ended = True
        if returnParameter == "Failure":
            CLI.PrintBoard(gameBoardState)
            print(f"\n\n\n {loseString} \n")
            ended = True
        if ended:
            while(True):
                print("Do you want to try again\t y/n")
                answer = input().lower().strip()
                if answer == "n":
                    sys.exit(0)
                    break
                elif answer == "y":
                    returnParameter = PlayerInput.Get_difficulty_player_cli()
                    ended = False
                    break
                else:
                    print("Wrong answer try again only n or y works")
        if re.fullmatch(r"^[0-9]$",returnParameter):
            difficulty = int(returnParameter)
            gameBoard, gameBoardState = GameBoard.CreateBoards(difficulty)
if __name__== "__main__":

    main()