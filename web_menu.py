from deck import Deck
from flask import Flask, render_template, request, redirect
from database import Database
import pokemon_download
import sqlite3

database = Database()

button_count = 0

app = Flask(__name__)

class Button:
    def __init__(self):
        self.check = False
        self.deck_a = []
        self.deck_b = []
        self.counter = -1

var = Button()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/game")
def game():
    global var
    try:
        deck=Deck()
    except sqlite3.OperationalError:
        return redirect("/")
    while var.check is False:
        deck = Deck()
        var.deck_a, var.deck_b = deck.shuffle()
        var.check = True
    else:
        var.counter += 1
        value = next(var.deck_a, var.deck_b, var.counter)
        values, values2, counter = value
        try:
            name, attack, defense, type1, type2 = values
            name2, attack2, defense2, types1, types2 = values2
        except TypeError:
            name, attack, defense, type1 = values
            name2, attack2, defense2, types1, = values2
        return render_template('game_template.html', deck_a=var.deck_a, deck_b=var.deck_b, name=name, attack=attack, defense=defense,
                               type1=type1, type2 = type2, name2=name2, attack2=attack2, defense2=defense2, types1 = types1, types2=types2, counter=counter)

def next(deck_a, deck_b, counter):
    database = Database()
    values = database.pokemonData(deck_a, counter)
    values2 = database.pokemonData(deck_b, counter)
    return values, values2, counter

@app.route("/test")
def test():
    return render_template('test.html')
@app.route("/pokedex")
def display_pokedex():
    return render_template('pokedex.html')

@app.route("/downloadPokemons")
def download_pokemons():
    global button_count
    if button_count % 2 == 0:
        try:
            database.delete_table()
        except sqlite3.OperationalError:
            pass
        database.createTables()
        pokemon_download.getPokemon(database)
        alert = 'Do you want to override pokemon data? If yes, click Download Pokemons again'
    else:
        alert = None
    button_count += 1
    names = database.returnNames()
    names_list = names.values.tolist()
    return render_template('pokedex.html', names=names_list, alert=alert)

@app.route("/showPokemons")
def show_pokemons():
    names = database.returnNames()
    names_list = names.values.tolist()
    name = request.args.get('name')
    data = database.getAll(name)
    data_list = data.values.tolist()
    return render_template('card.html', names=names_list, name=data_list[0][1], art=data_list[0][2],
                           attack=data_list[0][3], defense=data_list[0][4], type=data_list[0][5], type2 = data_list[0][6])

if __name__ == "__main__": app.run()
