from flask import Flask, render_template, redirect
from create_deck import Deck
import pokemon_download
import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('pokedex.db', check_same_thread=False)
except Error as e:
    print(e)
    raise e
cursor = conn.cursor()

class GamMan:

    def __init__(self):
        try:
            self.conn = sqlite3.connect('pokedex.db', check_same_thread=False)
        except Error as e:
            print(e)
            raise e
        self.cursor = self.conn.cursor()

    def checkData(self):
        deck=Deck()
        decks = deck.shuffle()
        deck_a, deck_b = decks
        if len(deck_a) < 1:
            return redirect("/")
        else:
            return render_template('game_template.html')

def pokemon_data(deck):
    pokemon_find = deck[0]
    find_pokemon = """
        SELECT Name, Attack, Defense, Types
        FROM Pokedex
        WHERE ID=?
                """
    cursor.execute(find_pokemon, (pokemon_find,))
    data = cursor.fetchone()
    return data
