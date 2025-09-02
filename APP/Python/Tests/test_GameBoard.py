import unittest
import time
from GameBoard import GameBoard

class TestGameBoard(unittest.TestCase):

    def test_populate_With_Bombs(self):
        size = 5
        maxbombs = 4
        gameBoard = [[0 for c in range(size)] for r in range(size)]
        GameBoard.Pubulate_gameBoardState_with_bombs(gameBoard,maxbombs,size)
        number_of_bombs_found = 0
        for row in gameBoard:
            for col in row:
                if col == "X":
                    number_of_bombs_found +=1
        self.assertEqual(number_of_bombs_found,maxbombs)

    def test_populate_with_numbers(self):
        '''
        Created an 2d array with all field be 1 and the middle be a bomb. and test that the method created the same
        '''

        size = 3
        gameBoard = [[0 for c in range(size)] for r in range(size)]
        gameBoard[1][1] = "X"
        GameBoard.Pubulate_gameBoardState_with_numbers(gameBoard)
        true_gameBoard = [[1 for c in range(size)] for r in range(size)]
        true_gameBoard[1][1] = "X"
        self.assertEqual(gameBoard,true_gameBoard)
    
    def test_createBoard_difficulty(self):
        '''
        IT should not take more then 1 milisecound to create the board
        '''

        Timer= 1

        Start = time.time()
        GameBoard.CreateBoards(1)
        endTime = time.time()
        fullTime = (endTime - Start) * 1e3
        self.assertGreater(Timer,fullTime)

        Start1 = time.time()
        GameBoard.CreateBoards(2)
        endTime1 = time.time()
        fullTime1 = (endTime1 - Start1) * 1e3
        self.assertGreater(Timer,fullTime1)

        Start2 = time.time()
        GameBoard.CreateBoards(2)
        endTime2 = time.time()
        fullTime2 = (endTime2 - Start2) * 1e3
        self.assertGreater(Timer,fullTime2)


if __name__ =="__main__":
    unittest.main()