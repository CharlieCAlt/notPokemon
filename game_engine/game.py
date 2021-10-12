from deck import Deck
from game_engine.player import Player
import numpy as np
from database import Database
import pokemon_download


class Game:

    def __init__(self):
        database = Database()
        database.delete_table()
        database.createTables()
        pokemon_download.getPokemon(database)
        self.deck = Deck()
        deck_a, deck_b = self.deck.shuffle()
        self.player_1 = Player(1)
        self.player_2 = Player(2)
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
        attacker = self.attacker
        defender = self.defender
        deck = self.deck
        attack = deck.get_attack(attacker.deck, deck.counter)
        defense = deck.get_defense(defender.deck, deck.counter)
        # modify damage based on type
        # type_attacker = get_type(self.attacker)
        # type_defender = get_type(self.defender)
        if attack > defense:
            result = 'won'
            attacker.deck.append(defender.deck[deck.counter])
            del defender.deck[deck.counter]
        else:
            result = 'lost'
            defender.deck.append(attacker.deck[deck.counter])
            del attacker.deck[deck.counter]
            self.attacker = defender
            self.defender = attacker
        return result

    def finish(self):
        winner = None
        if len(self.player_1.deck) == 0:
            winner = self.player_2
            self.finished = True
        if len(self.player_2.deck) == 0:
            winner = self.player_1
            self.finished = True
        return winner



