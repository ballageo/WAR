class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.discard = []
        self.wins = 0

    def __str__(self):
        return f"Name: {self.name}" 

    def print_hand(self):
        for i in range(0, len(self.hand)):
            print(self.hand[i])