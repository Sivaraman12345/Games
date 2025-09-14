class Game:
    def __init__(self):
        self.cells=[None]*9

    def display(self) ->None:
        print("\n"+"="*15)
        cell1=self.cells[i*3] if self.cells[i*3] else i*3+1
        cell2=self.cells[i*3+1] if self.cells[i*3+1] else i*3+2
        cell3=self.cells[i*3+2] if self.cells[i*3+2] else i*3+3
        
        for i in range(3):
            print(f"{cell1} | {cell2} | {cell3}")
            if i<2: print("\n"+"-"*6+"+"+"_"*6)
        print("\n"+"="*15)





        
    def make_move(self,pos,sym)->bool:
        indx=pos-1
        if pos<1 or pos>9:
            return False
        if self.cells[indx] is None:
            self.cells[indx]=sym
            return True
        return False
    
    def draw_check(self) -> bool:
        return all(i is not None for i in self.cells)
        
    def win_check(self,sym) -> bool:
        pass



gam=Game()
gam.display