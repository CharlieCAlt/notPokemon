import random
from database import Database

class Deck:
    def __init__(self):
        database = Database()
        database.cursor.execute("SELECT * FROM Pokedex")
        results = database.cursor.fetchall()
        self.full_deck = list(range(1, len(results)+1))
        self.check = False
        self.deck_a = []
        self.deck_b = []
        self.counter = -1

    def shuffle(self):
        half = len(self.full_deck)/2
        half = int(half)
        random.shuffle(self.full_deck)
        random_number = random.randint(0, 99)
        if random_number in range(0, 49):
            deck_a = self.full_deck[:half]
            deck_b = self.full_deck[half:]
        else:
            deck_b = self.full_deck[:half]
            deck_a = self.full_deck[half:]
        return deck_a, deck_b

    def next_card(self, deck_a, deck_b, counter):
        database = Database()
        values = database.pokemonData(deck_a, counter)
        values2 = database.pokemonData(deck_b, counter)
        return values, values2, counter

    def get_attack(self, deck):
        database = Database()
        attack = database.get_attack(deck)
        return attack

    def get_defense(self, deck):
        database = Database()
        defense = database.get_defense(deck)
        return defense

    def get_types(self, deck):
        database = Database()
        types = database.get_types(deck)
        return types
