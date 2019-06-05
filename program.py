from Deck import Deck
from Player import Player
from war import War

if __name__ == "__main__":
    deck = Deck()
    Jon = Player("Jon Snow")
    Dave = Player("David Spade")
    war = War(Jon, Dave)
    deck.build_deck()
    deck.shuffle()
    war.deal(deck)

    # print(Dave)
    # # Dave.print_hand()
    # print(Jon)
    # Jon.print_hand()
    war.play_game()
    deck.shuffle()