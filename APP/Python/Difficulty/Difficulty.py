def getDifficultyStats(Difficulty:int):
    '''
    Difficultystats is a list with 3 attributes
    1: max mines
    2: width and hieght of game board
    3: difficultystr
    '''
    DifficultyStats=[]
    if Difficulty == 1:
        DifficultyStats.append(10)
        DifficultyStats.append(9)
        DifficultyStats.append("beginner")
    elif Difficulty == 2:
        DifficultyStats.append(40)
        DifficultyStats.append(16)
        DifficultyStats.append("Intermediate")
    elif Difficulty == 3:
        DifficultyStats.append(99)
        DifficultyStats.append(24)
        DifficultyStats.append("Advanced")
    else:
        DifficultyStats.append("Error")
    
    return DifficultyStats