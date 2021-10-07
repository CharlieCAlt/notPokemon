from flask import Flask, render_template, redirect
from create_deck import Deck
from create_tables import Database

app = Flask(__name__)
check = False
deck_a = []
deck_b = []
counter = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/game")
def game():
    global deck_a, deck_b, check, counter
    while check is False:
        deck = Deck()
        deck_a, deck_b = deck.shuffle()
        check = True
    if len(deck_a) < 1:
        return redirect("/")
    else:
        value = next(deck_a, deck_b, counter)
        values, values2, counter = value
        name, attack, defense, types = values
        name2, attack2, defense2, types2 = values2
        return render_template('game_template.html', deck_a=deck_a, deck_b=deck_b, name=name, attack=attack, defense=defense, types=types, name2=name2, attack2=attack2, defense2=defense2, types2=types2, counter=counter)

def next(deck_a, deck_b, counter):
    database = Database()
    counter += 1
    values = database.pokemonData(deck_a, counter)
    values2 = database.pokemonData(deck_b, counter)
    return values, values2, counter


@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == "__main__": app.run()
