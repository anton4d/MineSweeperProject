import unittest
import io
import sys

from PlayerInterface import CLI

class TestCLi(unittest.TestCase):

    def test_Abc_1(self):
        data = 1
        result = CLI.GetABCFromNumber(data)
        self.assertEqual(result,"A","Should be A")

    def test_Abc_27(self):
        data = 27
        result = CLI.GetABCFromNumber(data)
        self.assertEqual(result,"AA","Should be ZA")
    
    def test_Abc_53(self):
        data = 53
        result = CLI.GetABCFromNumber(data)
        self.assertEqual(result,"BA","Should be ZZA")

    def test_printline_three_columns(self):
        captured = io.StringIO()
        sys.stdout = captured
        CLI.PrintLine([1, 2, 3])
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\t  --- --- ---\n")

    def test_printline_empty(self):
        captured = io.StringIO()
        sys.stdout = captured
        CLI.PrintLine([])
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\t \n")

    def test_printrow_empty(self):
        captured = io.StringIO()
        sys.stdout = captured
        CLI.PrintRow([],1)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(),"1:\t |\n")

    def test_printrow_three_columns(self):
        captured = io.StringIO()
        sys.stdout = captured
        CLI.PrintRow([1,2,3],1)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(),"1:\t | 1 | 2 | 3 |\n")
    
    def test_printrow_firstline(self):
        captured = io.StringIO()
        sys.stdout = captured
        CLI.PrintRow([1,2,3],1,True)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(),"\t   A   B   C\n")

    def test_printgamestats(self):
        captured = io.StringIO()
        sys.stdout = captured
        dif = 1
        mf = 4
        tm = "10sec"
        CLI.PrintGameStats(dif,mf,tm)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(),f"Mines: {mf}/10\tTime: {tm}\tdifficulty: beginner\n")


if __name__ =="__main__":
    unittest.main()