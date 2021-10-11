from deck import Deck
from flask import Flask, render_template, request, redirect
from database import Database
import pokemon_download

database = Database()

button_count = 0

app = Flask(__name__)

class Button:
    def __init__(self):
        self.deck_a = []
        self.deck_b = []
        self.counterA = 70
        self.counterB = 70
        deck = Deck()
        self.deck_a, self.deck_b = deck.shuffle()


var = Button()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/game")
def game():
    return render_template('game_template.html')


@app.route("/cardStatsA")
def cardA():
    global var
    remaining_a = len(var.deck_a) - var.counterA
    if remaining_a == 0:
        var.counterA = 0
        remaining_a = len(var.deck_a) - var.counterA
    database = Database()
    values = database.pokemonData(var.deck_a, var.counterA)
    name, attack, defense, types = values
    var.counterA += 1
    return render_template('cardStatsA.html', deck_a=var.deck_a, name=name, attack=attack, defense=defense, types=types, counter1=var.counterA-1, remaining1=remaining_a)


@app.route("/cardStatsB")
def cardB():
    global var
    remaining_b = len(var.deck_b) - var.counterB
    if remaining_b == 0:
        var.counterB = 0
        remaining_b = len(var.deck_b) - var.counterB
    database = Database()
    values2 = database.pokemonData(var.deck_b, var.counterB)
    name2, attack2, defense2, types2 = values2
    var.counterB += 1
    return render_template('cardStatsB.html', deck_b=var.deck_b, name2=name2, attack2=attack2, defense2=defense2, types2=types2, counter2=var.counterB-1, remaining2=remaining_b)


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
        database.delete_table()
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
                           attack=data_list[0][3], defense=data_list[0][4], type=data_list[0][5])


if __name__ == "__main__": app.run()
