from flask import Flask, render_template, redirect
from create_deck import Deck
from create_tables import Database

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/game")
def game():
    deck=Deck()
    deck_a, deck_b = deck.shuffle()
    if len(deck_a) < 1:
        return redirect("/")
    else:
        database = Database()
        values = database.pokemonData(deck_a)
        values2 = database.pokemonData(deck_b)
        name, attack, defense, types = values
        name2, attack2, defense2, types2 = values2
        return render_template('game_template.html', deck_a = deck_a, deck_b=deck_b, name=name, attack=attack, defense=defense, types=types, name2=name2, attack2 = attack2, defense2 = defense2, types2 = types2)

@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == "__main__": app.run()
