class Board:
    #constructor
    def __init__(self):
        self.grid=[[' ' for i in range(3)] for j in range(3)]
        filledCells=0
    
    #show board
    def show_board(self):
        for i in range(3):
            for j in range(3):
                print(self.grid[i][j], end=' ')
                if j<2:
                    print(" | ",end=' ')
            if i<2:
                print("\n--------------")
    def valid_move(self,position,filledcells):
        if position<0 or position>9:
            f
    
    def mark_move(self,position,symbol):
        is valid_move(position):
            a=position/3
            b=position%3
            self.grid[a][b]=symbol

class Player:
    def __init__(self):
        self.symbol='X'
        currentPlayer=1
    




b=Board()
b.show_board()