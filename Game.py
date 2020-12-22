#!/usr/bin/python

from Board import *
from Player import *
#from tkinter import *

class Game_engine():
    def __init__(self):
        self.player1=Player("player1","white")
        self.player2=Player("player2","black")
        self.currentPlayer=self.player1
        
        self.GUI=Board(self)

    def checkIfMoveIsLegal(self,row,column,game):
        currentPlayer=self.getCurrentPlayer()
        normalMoveDirPlayer1 = [[-1, -1], [-1, 1]]
        captureMoveDirPlayer1 = [[-2, -2], [-2, 2]]
        normalMoveDirPlayer2 = [[1,1],[1,-1]]
        captureMoveDirPlayer2 =[[2,2],[2,-2]]

        if currentPlayer.color=="white":
            usableNormalMove=normalMoveDirPlayer1
            usableCaptureMove=captureMoveDirPlayer1
        else:
            usableNormalMove=normalMoveDirPlayer2
            usableCaptureMove=captureMoveDirPlayer2

        normalMoves=[]
        captureMoves=[]

        for dir in usableNormalMove:
            if game.checkIfSpotEmpty(row+dir[0],column+dir[1]):
                normalMoves.append([row+dir[0],column+dir[1]])
        
        for dir in usableNormalMove:
            if game.checkIfEnemyPiece(row+dir[0],column+dir[1]):
                for dir2 in usableCaptureMove:
                    if abs(dir2[1]-dir[1])==1:
                        if game.checkIfSpotEmpty(row+dir2[0],column+dir2[1]):
                            captureMoves.append([row+dir2[0],column+dir2[1]])
        
        if captureMoves:
            return captureMoves
        else:
            return normalMoves
            
    def getCurrentPlayer(self):
        return self.currentPlayer

    def changeCurrentPlayer(self):
        if self.currentPlayer==self.player1:
            self.currentPlayer=self.player2
        else:
            self.currentPlayer=self.player1