from database import Database
import pokemon_download
from sqlite3 import IntegrityError
from deck import Deck

def main():
    print(pokemon_download.damageModifier('fighting', 'rock', ''))


if __name__ == '__main__':
    main()