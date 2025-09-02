from Difficulty import getDifficultyStats
from PlayerInterface import CLI
import random

def CreateBoards(Difficulty):
    gameStats = getDifficultyStats(Difficulty)
    size = gameStats[1]
    MaxMines = gameStats[0]
    gameBoard = [["?" for c in range(size)] for r in range(size)]
    gameBoardState = [["0" for i in range(size)] for j in range(size)]

    Pubulate_gameBoardState_with_bombs(gameBoardState,MaxMines,size)
    Pubulate_gameBoardState_with_numbers(gameBoardState)

    return gameBoard, gameBoardState

def Pubulate_gameBoardState_with_bombs(gameBoardState,MaxMines,size):
    for m in range(MaxMines):
        while(True):
            x,y = get_Random_x_y(size)
            if gameBoardState[x][y] != "X":
                gameBoardState[x][y] = "X"
                break


def get_Random_x_y(size):
    x = random.randrange(size)
    y = random.randrange(size)
    return x,y

def Pubulate_gameBoardState_with_numbers(gameBoardState):
    r = 0
    c = 0
    for row in gameBoardState:
        for col in row:
            if col == "X":
                update_Around(r,c,gameBoardState)
            c+=1
        c =0
        r+=1

def update_Around(r,c,gameBoardState):
    tempr = r - 1
    for y in range(3):
        tempc = c - 1
        if tempr == -1 or tempr >= len(gameBoardState):
            tempr += 1
            continue
        for t in range(3):
            if tempc == -1 or tempc >= len(gameBoardState):
                tempc +=1
                continue
            gameBoardStateValue = gameBoardState[tempr][tempc]
            if gameBoardStateValue != "X":
                gameBoardStateValue = int(gameBoardStateValue)
                gameBoardState[tempr][tempc] = gameBoardStateValue + 1
            tempc +=1
        tempr += 1


if __name__ == "__main__":
    GameBoard, GameBoardState = CreateBoards(1)
    print(GameBoardState)
    CLI.PrintBoard(GameBoardState)

