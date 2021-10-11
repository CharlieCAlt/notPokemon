from database import Database


class Button:
    def __init__(self):
        self.check = False
        self.deck_a = []
        self.deck_b = []
        self.counter = -1

    def next_card(self,deck_a, deck_b, counter):
        database = Database()
        values = database.pokemonData(deck_a, counter)
        values2 = database.pokemonData(deck_b, counter)
        return values, values2, counter