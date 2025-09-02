import unittest

from GameBoard.GameBoard import GameBoard

class TestGameBoard(unittest.TestCase):

    def test_populate_With_Bombs(self):
        size = 5
        maxbombs = 4
        gameBoard = [["0" for c in range(size)] for r in range(size)]
        GameBoard.Pubulate_gameBoardState_with_bombs(gameBoard,maxbombs,size)
        number_of_bombs_found = 0
        for row in gameBoard:
            for col in row:
                if col == "X":
                    number_of_bombs_found +=1
        self.assertEqual(number_of_bombs_found,maxbombs)

if __name__ =="__main__":
    unittest.main()