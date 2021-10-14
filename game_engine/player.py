from deck import Deck

class Player:

    def __init__(self, player_no):
        self.attacker = False
        self.defender = False
        self.deck = None
        self.player_no = player_no
        self.counter = 0
        self.win = False

    def __str__(self):
        return f'Player {self.player_no}'

