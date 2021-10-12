from database import Database
import pokemon_download
from sqlite3 import IntegrityError
from deck import Deck
from game_engine.game import Game

def main():
    game = Game()
    game.choose_attacker()
    print(game.attacker)
    game.attack()


if __name__ == '__main__':
    main()