from Difficulty import getDifficultyStats
import re



def Get_difficulty_player_cli():
    '''
    Asks the user for the difficulty with the prompt being the list of difficulties
    returns difficulty as a int
    '''
    prompt = "Here is a list of difficulties:\n\n"
    x = 1
    while(True):
        stats = getDifficultyStats(x)
        if stats[0] == "Error":
            break
        prompt += f"{x}:{stats[2]}\nMax mines: {stats[0]}\nBoardSize: {stats[1]}\n\n"
        x +=1
    
    prompt += "Choose difficulty by its number"
    diffy = input(prompt).strip()
    return diffy

def Take_command_cli(GameBoard, gameState,Minesfound,difficulty):
    command_map = {
        "help": (lambda: Print_commands(command_map),"Show available commands"),
        "h": (lambda: Print_commands(command_map),"Show available commands"),
        "x": (lambda: Mark_a_flag(GameBoard, Minesfound),"Mark a Mine on the board"),
        "mine": (lambda: Mark_a_flag(GameBoard, Minesfound),"Mark a flag on the board"),
        "flag": (lambda: Mark_a_flag(GameBoard, Minesfound),"Mark a flag on the board"),
        "step": (lambda: Step_on_space(GameBoard, gameState,difficulty),"Step on a space"),
        "dig": (lambda: Step_on_space(GameBoard, gameState,difficulty),"Step on a space"),
        "difficulty":(lambda:Get_difficulty_player_cli(),"Change Difficulty and reset"),
        "d":(lambda:Get_difficulty_player_cli(),"Change Difficulty and reset")
    }
    prompt = "Write Command:\t"
    ErrorMessage="Unknown command. Type 'help' for options."
    ReturnParameter = ""

    command = input(prompt).strip()
    normalized = command.lower()
    coord_pattern = r"^[A-Za-z]+[0-9]+$"

    if re.fullmatch(coord_pattern, command):
        ReturnParameter = Step_on_space(GameBoard, gameState,difficulty, command.upper())
    else:
        entry = command_map.get(normalized)
        if entry:
            func, desc = entry   
            ReturnParameter = func()   
        else:
            print(ErrorMessage)
    
    return ReturnParameter
        

def Print_commands(command_map):
    PrintString = "Commands:\n"
    for cmd, (func, desc) in command_map.items():
        PrintString += f"{cmd}:\t{desc}\n"
    print(PrintString)
    return "Help"
    
def Check_If_position_is_in_square(GameBoard,row,col):
    if row == "error" or row > len(GameBoard) or col > len(GameBoard):
        return True
    return False

def Mark_a_flag(GameBoard,Minesfound,rc = None):
    prompt = "What square do you want to mark with a flag\nAs: A1\n"
    if rc != None:
        row , col = parse_position(rc)
    else:
        Position = input(prompt)
        row,col = parse_position(Position)

    if Check_If_position_is_in_square(GameBoard,row,col):
        return "error"
    
    GameBoard[row][col] = "F"
    Minesfound["count"] += 1
    return "Flag"

def Step_on_space(GameBoard,GameState,difficulty,rc=None):
    prompt="What square do you want to step on\nAs: A1\n"
    row,col = None,None
    if rc != None:
        row , col = parse_position(rc)
    else:
        Position = input(prompt)
        row,col = parse_position(Position)

    if Check_If_position_is_in_square(GameBoard,row,col):
        return "error"
    
    if Check_if_lost(GameState,row,col):
        return "Failure"

    if GameState[row][col] == 0:
        Zero_Updater(GameBoard,GameState,row,col)
    else:
        GameBoard[row][col] = GameState[row][col]

    if Check_if_wone(GameBoard,difficulty):
        return "Success"
    
    return "Step"


def Zero_Updater(GameBoard,GameState,Row,Col):
    cords = [(Row,Col)]
    for cord in cords:
        r,c = cord
        GameBoard[r][c] = GameState[r][c]
        tempr = r - 1
        for y in range(3):
            tempc = c - 1
            if tempr == -1 or tempr >= len(GameState):
                tempr += 1
                continue
            for t in range(3):
                if tempc == -1 or tempc >= len(GameState) or (tempr == r and tempc == c):
                    tempc +=1
                    continue
                gameBoardStateValue = GameState[tempr][tempc]
                if gameBoardStateValue == 0:
                    if (tempr,tempc) not in cords:
                        cords.append((tempr,tempc))
                else:
                    GameBoard[tempr][tempc] = GameState[tempr][tempc]
                tempc +=1
            tempr += 1

def Check_if_wone(GameBoard,difficulty):
    count = 0
    mines = getDifficultyStats(difficulty)
    for row in GameBoard:
        for col in row:
            print(col)
            if col == "?":
                count +=1
    print(count)
    print(mines)
    if count <= mines[1]:
        
        return True
    return False

def Check_if_lost(GameState,row,col):
    if GameState[row][col] == "X":
        return True
    return False


def parse_position(pos: str):
    """Parse a position string like 'A1' or 'BC12' into (row, column)."""
    match = re.match(r"([A-Z]+)(\d+)", pos.upper())
    if not match:
        print(f"Invalid position: {pos}")
        return "error", "error"
    
    col_letters, row_str = match.groups()
    row = int(row_str)
    
    col = 0
    for ch in col_letters:
        col = col * 26 + (ord(ch) - ord("A") + 1)
    col = col -1
    row = row -1
    return row, col

if __name__ == "__main__":
    size = 3
    gameBoard = [["?" for c in range(size)] for r in range(size)]
    gameBoardState = [[0 for i in range(size)] for j in range(size)]
    MinesFound = {"count": 0}
    #print(Get_difficulty_player_cli())
    #some=  Take_command_cli(gameBoard,gameBoardState,minesfound)
    #print(parse_position("A1"))
    #print(parse_position("AB1"))
