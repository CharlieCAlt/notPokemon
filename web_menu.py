from deck import Deck
from flask import Flask, render_template, request, redirect
from database import Database
import pokemon_download
from button import Button

app = Flask(__name__)

database = Database()

var = Button()

button_count = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/game")
def game():
    global var
    while var.check is False:
        deck = Deck()
        var.deck_a, var.deck_b = deck.shuffle()
        #print(var.deck_a, var.deck_b)
        var.check = True
    if len(var.deck_a) < 1:
        return redirect("/")
    else:
        var.counter += 1
        value = var.next_card(var.deck_a, var.deck_b, var.counter)
        values, values2, counter = value
        name, attack, defense, types = values
        name2, attack2, defense2, types2 = values2
        return render_template('game_template.html', deck_a=var.deck_a, deck_b=var.deck_b, name=name, attack=attack, defense=defense, types=types, name2=name2, attack2=attack2, defense2=defense2, types2=types2, counter=counter)


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
