from Card import Card
from Player import Player
from random import randint

class Deck:
    def __init__(self):
        self.cards = []
        self.size = 52
        self.suits = ["spades", "hearts", "clubs", "diamonds"]
        self.faces = [ "Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2" ]
        self.values = [ 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2 ]

    def build_deck(self):
        for suit in self.suits:
            for i in range(len(self.values)):
                self.cards.append(Card(suit, self.faces[i], self.values[i])) 

    def print_deck(self):
        for card in self.cards:
            print(card)

    def print_hand(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        for i in range(self.size):
            index_to_swap = randint(0, self.size-1)
            self.cards[i], self.cards[index_to_swap] = \
                self.cards[index_to_swap], self.cards[i]
