'''
Created on Apr 24, 2016

@author: Jordan Handwerger

Pledge: I pledge my honor that I have abided by the Stevens Honor System. JH
'''
class Board(object):
    def __init__(self, width=7, height=6):
        self.__width = width
        self.__height = height
        self.__board = self.createBoard()
        
    def createBoard(self):
        '''Returns an empty board given the objects width and height'''
        board = []
        for row in range(self.__height):
            newRow = []
            for col in range(self.__width):
                newRow += [' ']
            board += [newRow]
        return board
    
    def __str__(self):
        """String overload prints a connect four type board."""
        newStr = ''
        for row in range(self.__height):
            newRow = ''
            for col in range(self.__width):
                newRow += '|' + self.__board[row][col]
            newStr += newRow + '|\n'
        newStr += '-' * (self.__width + 1)* 2 + '\n'
        for i in range(self.__width):
            newStr += ' ' + str(i)
        return newStr
    
    def allowsMove(self, col):
        '''Returns True if another move can be done in the given column, false if not.'''
        try:
            int(col)
        except:
            return False
        col = int(col)
        if col not in list(range(self.__width)):
            return False
        else:
            for row in self.__board:
                if row[col] == ' ':
                    return True
            return False
        
    def addMove(self, col, ox):
        '''Adds an ox character in the given column if possible.'''
        if self.allowsMove(col) == True:
            addRow = -1
            for row in self.__board:
                if row[col] == ' ':
                    addRow += 1
                else:
                    break
            self.__board[addRow][col] = ox
        
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
         alternating checkers in those columns,
         starting with 'X'
        
         For example, call b.setBoard('012345')
         to see 'X's and 'O's alternate on the
         bottom row, or b.setBoard('000000') to
         see them alternate in the left column.
         moveString must be a string of integers
         """
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                    self.addMove(col, nextCh)
                    if nextCh == 'X': nextCh = 'O'
                    else: nextCh = 'X'
                    
    def delMove(self, col):
        """Deletes the last move made in a given column."""
        for row in self.__board:
            if row[col] != ' ':
                row[col] = " "
                break
    
    def winsFor(self, ox):
        """Returns True if ox, the given play, has won horizontally, vertically, or diagonally. False if not."""
        #horizontal check
        for row in range(self.__height):
            horCount = 0
            for col in range(self.__width):
                if self.__board[row][col] == ox:
                    horCount +=1
                    if horCount >= 4:
                        return True
                else:
                    horCount = 0

        
        #vertical check.
        for col in range(self.__width):
            vertCount = 0
            for row in range(self.__height):
                if self.__board[row][col] == ox:
                    vertCount += 1
                    if vertCount >= 4:
                        return True
                else:
                    vertCount = 0
                    
        #diagonal check for diagonals staring at the top row
        # and moving down to the right
        for col in range(self.__width):
            x = col
            y = 0
            diagCount = 0
            while y < self.__height and x < self.__width:
                if self.__board[y][x] == ox:
                    diagCount += 1
                    if diagCount >= 4:
                        return True
                    else:
                        y += 1
                        x += 1
                else:
                    diagCount = 0
                    y += 1
                    x += 1 
        #diagonal check for all diagonals starting from the left column 
        # and moving down to the right           
        for row in range(self.__height):
            x = 0
            y = row
            diagCount = 0
            while y < self.__height and x < self.__width:
                if self.__board[y][x] == ox:
                    diagCount += 1
                    if diagCount >= 4:
                        return True
                    else:
                        y += 1
                        x += 1
                else:
                    diagCount = 0
                    y += 1
                    x += 1
        #diagonal check for all diagonals starting from the bottom row
        # and moving up to the right           
        for col in range(self.__width):
            x = col
            y = self.__height - 1
            diagCount = 0
            while y > -1 and x < self.__width:
                if self.__board[y][x] == ox:
                    diagCount += 1
                    if diagCount >= 4:
                        return True
                    else:
                        y -= 1
                        x += 1
                else:
                    diagCount = 0
                    y -= 1
                    x += 1 
        
        #diagonal check for all diagonals starting in the left column
        # and moving up to the left.           
        for row in range(self.__height):
            x = 0
            y = row
            diagCount = 0
            while y > -1 and x < self.__width:
                if self.__board[y][x] == ox:
                    diagCount += 1
                    if diagCount >= 4:
                        return True
                    else:
                        y -= 1
                        x += 1
                else:
                    diagCount = 0
                    y -= 1
                    x += 1
        
        return False
    
    def hostGame(self):
        """Provides the text interface of the game"""
        print("Welcome to Connect Four!\n")
        while True:
            print(self, '\n')
            X = input("X player enter your column choice.\n")
            while True:
            #X move input
                if self.allowsMove(X) == True:
                    print("X's choice: " + X + "\n")
                    self.addMove(int(X), "X")
                    print(self, '\n')
                    break
                else:
                    X = input(X + " is not a valid move." + " X player enter a valid column choice.\n")
                    
            if self.winsFor("X") == True:
                print("X wins -- Congratulations!")
                break
            
            #O move input
            O = input("O player enter your column choice.\n")
            while True:
                if self.allowsMove(O) == True:
                    print("O's choice: " + O)
                    self.addMove(int(O), "O")
                    print(self, "\n")
                    break
                else:
                    O = input(O + " is not a valid move." + " O player enter a valid column choice.\n")
                    
            
            if self.winsFor("O") == True:
                print("O wins -- Congratulations!")
                break
                
            
            
    
                    
        
                                   
if __name__ == "__main__":

    a = Board()
    a.hostGame()
