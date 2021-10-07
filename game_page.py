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
        pass

    def checkData(self):
        deck=Deck()
        decks = deck.shuffle()
        deck_a, deck_b = decks
        if len(deck_a) < 1:
            return redirect("/")
        else:
            return render_template('game_template.html')

#
# deck = Deck()
# deck_a, deck_b = deck.shuffle()
#
# print(deck_a)

def pokemon_data(deck_a):
    pokemon_find = deck_a[0]
    pokemon_find = str(pokemon_find)
    print(type(pokemon_find))
    find_pokemon = """
        SELECT Name, Attack, Defense, Types
        FROM Pokedex
        WHERE ID=?
                """
    cursor.execute(find_pokemon, (pokemon_find,))
    data = cursor.fetchone()
    return data

# print(pokemon_data())
# answer=pokemon_data()
# name, attack, defense, types = answer
# print(name)