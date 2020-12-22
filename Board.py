#!/usr/bin/python

from tkinter import *
from Game import *

class Board():
    def __init__(self,game):
        self.game=game
        self.ROWS=8
        self.COLUMNS=8
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 800
        self.col_width = self.WINDOW_WIDTH / self.COLUMNS
        self.row_height = self.WINDOW_HEIGHT / self.ROWS
        self.initBoard()

    def initBoard(self):
        self.root = Tk()
        self.c = Canvas(self.root, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT,
                                borderwidth=5, background='white')
        self.c.pack()
        self.checkers = [[None for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                if (row + column) % 2 == 1:
                    self.checkers[row][column]=self.c.create_rectangle(row * self.row_height, column * self.col_width,
                                        (row+1) * self.row_height, (column+1) * self.col_width, fill="gray")
        
        self.populateboard()
        self.c.bind("<Button-1>", self.processClick)
        
        self.isCheckerSelected=False
        self.oldcheckerStatus={"row":0,"col":0}
        self.root.after(1000)
        #part to comment out if want to do unit testing
        self.startGUI()
    
    def populateboard(self):
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                if row<(self.ROWS/2-1):
                    if (row+column)%2==1:
                        self.checkers[row][column]=self.c.create_oval(column*self.col_width+10, row*self.row_height+10,
                                                              (column+1)*self.col_width-10, (row+1)*self.row_height-10,
                                                              fill="black")

                if row>(self.ROWS/2):
                    if (row+column)%2==1:
                        self.checkers[row][column]=self.c.create_oval(column*self.col_width+10, row*self.row_height+10,
                                                              (column+1)*self.col_width-10, (row+1)*self.row_height-10,
                                                              fill="white")

    def startGUI(self):
        self.root.mainloop()

    def processClick(self, event):
        column = int(event.x // self.col_width)
        row = int(event.y // self.row_height)
        currentPlayer=self.game.getCurrentPlayer()

        if not self.isCheckerSelected:
            if currentPlayer.color==self.c.itemcget(self.checkers[row][column], 'fill'):
                availableMoves=self.game.checkIfMoveIsLegal(row,column,self)
                if availableMoves:
                    #print(availableMoves)
                    self.createChecker(row,column,"green")
                    self.isCheckerSelected=True
                    self.oldcheckerStatus["row"]=row
                    self.oldcheckerStatus["col"]=column

        if self.isCheckerSelected:
            availableMoves=self.game.checkIfMoveIsLegal(self.oldcheckerStatus["row"],
                                                            self.oldcheckerStatus["col"],self)
            print(availableMoves)
            if [row,column] in availableMoves:
                if abs(row-self.oldcheckerStatus["row"])==2:
                    self.makeCaptureMove(row,column,currentPlayer.color,self.oldcheckerStatus["row"],self.oldcheckerStatus["col"])
                else:
                    self.makeNormalMove(row,column,currentPlayer.color,self.oldcheckerStatus["row"],self.oldcheckerStatus["col"])
                self.isCheckerSelected=False
                self.game.changeCurrentPlayer()    
  
    def checkIfSpotEmpty(self,row,column):
        if row>-1 and column>-1 and column<8 and row<8:
            if self.c.itemcget(self.checkers[row][column], 'fill')=="gray":
                return True
    
    def checkIfEnemyPiece(self,row,column):
        currentPlayer=self.game.getCurrentPlayer()
        if currentPlayer.color=="white":
            enemyColor="black"
        else:
            enemyColor="white"
        
        if row>-1 and column>-1 and column<8 and row<8:
            if self.c.itemcget(self.checkers[row][column], 'fill')==enemyColor:
                #print(self.c.itemcget(self.checkers[row][column], 'fill'))
                return True

    def makeNormalMove(self,row,column,color,oldRow,oldColumn):
        self.createChecker(row,column,color)
        self.createEmptySpot(oldRow,oldColumn)

    def makeCaptureMove(self,row,column,color,oldRow,oldColumn):
        if row>oldRow:
            transitioningRow=oldRow+1
        else:
            transitioningRow=oldRow-1

        if column>oldColumn:
            transitioningColumn=oldColumn+1
        else:
            transitioningColumn=oldColumn-1
        
        self.createChecker(row,column,color)
        self.createEmptySpot(transitioningRow,transitioningColumn)
        self.createEmptySpot(oldRow,oldColumn)

    def createChecker(self,row,column,color):
        self.checkers[row][column]=self.c.create_oval(column*self.col_width+10, row*self.row_height+10,
                                                              (column+1)*self.col_width-10, (row+1)*self.row_height-10,
                                                              fill=color)
        return self.c.itemcget(self.checkers[row][column], 'fill')

    def createEmptySpot(self,row,column):
        self.checkers[row][column]=self.c.create_rectangle(column*self.col_width, row*self.row_height,
                                                              (column+1)*self.col_width, (row+1)*self.row_height,
                                                              fill="gray")
        return self.c.itemcget(self.checkers[row][column], 'fill')
        



