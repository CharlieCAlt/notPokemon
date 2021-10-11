from deck import Deck
from player import Player


class Game:

    def __init__(self):
        deck = Deck()
        deck_a, deck_b = deck.shuffle()
        self.player_1 = Player()
        self.player_2 = Player()
        self.player_1_deck = deck_a
        self.player_2_deck = deck_b
        self.attacker = None
        self.defender = None

    def choose_attacker(self):
        pass

    def attack(self):
        pass

