from deck import Deck
from player import Player
import numpy as np


class Game:

    def __init__(self):
        self.deck = Deck()
        deck_a, deck_b = self.deck.shuffle()
        self.player_1 = Player()
        self.player_2 = Player()
        self.player_1.deck = deck_a
        self.player_2.deck = deck_b
        self.attacker = None
        self.defender = None
        self.finished = False

    def choose_attacker(self):
        number = np.random.randint(1,3)
        if number == 1:
            self.attacker = self.player_1
            self.defender = self.player_2
        if number == 2:
            self.attacker = self.player_2
            self.defender = self.player_1

    def attack(self):
        attack = self.deck.get_attack(self.attacker.deck, self.deck.counter)
        winner = self.attacker
        return winner


