from GameBoard import GameBoard
from PlayerInterface import CLI
from Difficulty import getDifficultyStats
from Actions import PlayerInput
import time,re


def main():
    difficulty = 1
    gameBoard, gameBoardState = GameBoard.CreateBoards(difficulty)
    MinesFound = {"count": 0}
    print("begin")
    TimeStart = time.time()
    while(True):
        print("\n\n\n\n")
        timeStamp= time.time() - TimeStart
        CLI.ShowGameState(gameBoard,difficulty,MinesFound,timeStamp)
        returnParameter = PlayerInput.Take_command_cli(gameBoard,gameBoardState,MinesFound,difficulty)
        if returnParameter == "Success":
            print("\n\n\n you Win!!!!\n")
            CLI.PrintBoard(gameBoardState)
            print("\n\n")
            CLI.PrintBoard(gameBoard)
            break
        if returnParameter == "Failure":
            print("\n\n\n you lose!!\n")
            CLI.PrintBoard(gameBoardState)
            
            break
        if re.fullmatch(r"^[0-9]$",returnParameter):
            difficulty = int(returnParameter)
            gameBoard, gameBoardState = GameBoard.CreateBoards(difficulty)
if __name__== "__main__":

    main()