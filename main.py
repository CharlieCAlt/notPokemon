from database import Database
import pokemon_download
from sqlite3 import IntegrityError
from deck import Deck

def main():
    database = Database()
    database.createTables()
    try:
        pokemon_download.getPokemon(database)
    except IntegrityError:
        pass
    deck = Deck()
    answer = deck.shuffle()
    deck_a, deck_b = answer

if __name__ == '__main__':
    main()