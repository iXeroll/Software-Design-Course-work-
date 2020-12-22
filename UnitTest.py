#!/usr/bin/python
# Kad veiktu testai reik isjungt GUI ijungima
import unittest
from Game import*
from Board import *

class TestingCheckers(unittest.TestCase):
    def testCheckerWhite(self):
        row=4
        column=3
        color="white"
        Game=Game_engine()
        
        expected="white"
        
        self.assertEqual(Board.createChecker(Game.GUI,row,column,color),expected)
        #pass
    
    def testCheckerBlack(self):
        row=4
        column=3
        color="black"
        Game=Game_engine()

        expected="black"
        
        self.assertEqual(Board.createChecker(Game.GUI,row,column,color),expected)

    def testEmptySpotCreation(self):
        row=4
        column=3
        Game=Game_engine()

        expected="gray"

        self.assertEqual(Board.createEmptySpot(Game.GUI,row,column),expected)


if __name__ == '__main__':
  unittest.main()