from Player import Player
from Deck import Deck

class War:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def deal(self, deck):
        for i in range(52):
            if i < 26:   
                self.player1.hand.append(deck.cards[i])
            else: 
                self.player2.hand.append(deck.cards[i])
                
    def play_game(self):
        player1count = 0
        player2count = 0
        ties = 0
        for i in range(len(self.player1.hand)):
        # print("test")
        # print(self.player1.hand[len(self.player1.hand)-1].value)
        # print(self.player2.hand[len(self.player2.hand)-1].value)
            if self.player1.hand[len(self.player1.hand)-1].value > self.player2.hand[len(self.player2.hand)-1].value:
                player1count+=1
                self.player1.hand.pop()
                self.player2.hand.pop()

            elif self.player1.hand[len(self.player1.hand)-1].value < self.player2.hand[len(self.player2.hand)-1].value:
                player2count+=1
                self.player2.hand.pop()
                self.player1.hand.pop()

            else: 
                ties+=1
                self.player1.hand.pop()
                self.player2.hand.pop()
        print(f"{self.player1.name} - {player1count}")
        print(f"{self.player2.name} - {player2count}")
        print(f"IT'S A TIE THIS MANY - {ties}")
        
        
        if player1count > player2count:
            print(f"{self.player1.name} wins!")
        elif player2count > player1count:
            print(f"{self.player2.name} wins!")
        else: 
            print("IT'S A TIE")
            
            
            
            
print("GITHUB IS THE WPRST")