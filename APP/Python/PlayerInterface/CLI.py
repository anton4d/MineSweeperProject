from Difficulty import getDifficultyStats


def ShowGameState(GameBoard,Difficulty,MinesFound,timeStamp):
    PrintGameStats(Difficulty,MinesFound,timeStamp)
    PrintBoard(GameBoard)

def PrintGameStats(Difficulty, MinesFound, TimeStamp):
    DifficultyStats = getDifficultyStats(Difficulty)
    MaxMines = DifficultyStats[0]
    DifficultyStr = DifficultyStats[2]
    mines = MinesFound["count"]
    minutes = TimeStamp // 60
    minutes = int(minutes)
    seconds = TimeStamp % 60
    seconds = int(seconds)
    
    print(f"Mines: {mines}/{MaxMines}\tTime: {minutes:02d}:{seconds:02d}\tDifficulty: {DifficultyStr}")


def PrintBoard(GameBoard):
    r=1
    for row in GameBoard:
        if(r==1):
            PrintRow(row,r,True)
            PrintLine(row)
        
        PrintRow(row,r)
        PrintLine(row)
        r +=1

def PrintRow(row,RowIndex,First=False):
    Spacing=" | "
    ABCSpacing= "   "
    End= " |"
    printrow=""
    c=1

    if First == True:
        printrow="\t"
        for col in row:
            printrow += ABCSpacing+GetABCFromNumber(c)
            c += 1
    else: 
        printrow += f"{RowIndex}"+":"
        printrow += "\t"
        for col in row:
            printrow += Spacing+ f"{col}"
        printrow +=End
    print(printrow)

def PrintLine(row):
    PrintString = "\t "
    for col in row:
        PrintString +=" ---"
    print(PrintString)

def GetABCFromNumber(Number):
    '''Takes a number shuch as 1 and returns the coresponding 1=A
        if a number goes over 26 it will probegate like this 
        27 will result in AA since 27 - 26 is 1
    '''
    result = ""
   
    while Number > 0:
        Number, remainder = divmod(Number - 1, 26)
        result = chr(65 + remainder) + result
    return result


if __name__ == "__main__":
    rows, cols = (5, 27)
    gameBoard = [["?" for i in range(cols)] for j in range(rows)]
    MinesFound= 5
    timeStamp=60
    Difficulty=2
    ShowGameState(gameBoard,Difficulty,MinesFound,timeStamp)
