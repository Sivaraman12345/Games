import random
class Game:
    def __init__(self):
        self.cells=[None]*9

    def display(self) ->None:
        
        for i in range(3):
            cell1=self.cells[i*3] if self.cells[i*3] else i*3+1
            cell2=self.cells[i*3+1] if self.cells[i*3+1] else i*3+2
            cell3=self.cells[i*3+2] if self.cells[i*3+2] else i*3+3
        
            print(f" {cell1} | {cell2} | {cell3}")
            if i<2: print("-"*3+"+"+"-"*3+"+"+"-"*3)
        

    def make_move(self,pos,sym)->bool:
        if not pos.isnumeric():
            return False
        pos=int(pos)
        if pos<1 or pos>9:
            return False
        indx=pos-1
        
        if self.cells[indx] is None:
            self.cells[indx]=sym
            return True
        print("This cell is already taken")
        return False
    
    def draw_check(self) -> bool:
        return all(i is not None for i in self.cells)
        
    def win_check(self,sym) -> bool:
        winl=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for c in winl:
            if all(self.cells[k]==sym for k in c):
                return True
        return False
def play_game():
    print("Welcome to the Tic Tac Toe Game")
    p1=input("Enter player X's name:")
    p2=input("Enter player O's name:")
    while True:
        if p2.lower()==p1.lower():
            p2=input("Enter a unique name:")
        else: break
    score1=score2=0
    while True:
        game=Game()
        current_player=random.choice(['X','O'])
        while True:
            #Get move from current player
            game.display()
            p=p1 if current_player=='X' else p2
            move=input(f"{p}'s move [{current_player}] Choose from (1-9):")
            if not (game.make_move(move,current_player)):
                print("Please enter a valid move")
                continue
            
            if game.win_check(current_player):
                game.display()
                print(f"Yay, {p} won the game")
                if current_player=='X': score1+=1
                else: score2+=1
                break
            if game.draw_check():
                print("Game draw")
                break
            if current_player=="X":
                current_player="O"
            else: current_player="X"
        new_game=input(f"Score Card:\n{p1}'s Score={score1}\n{p2}'s score={score2}\nType yes to play again or press any other key to exit:").strip().lower()
        if score1==3:
            print(f"{p1} won the deck")
            score1=score2=0
        elif score2==3: 
            print(f"{p2} won the deck")
            score1=score2=0
        if new_game!="yes": 
            print("See you again!")
            break
play_game()


