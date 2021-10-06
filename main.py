from create_tables import Database
import pokemon_download
from sqlite3 import IntegrityError
from create_deck import Deck

def main():
    database = Database()
    database.CreateTables()
    try:
        pokemon_download.getPokemon(database)
    except IntegrityError:
        pass
    deck = Deck()
    answer = deck.shuffle()
    deck_a, deck_b = answer
    print(deck_a)

if __name__ == '__main__':
    main()