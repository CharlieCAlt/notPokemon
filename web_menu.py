from flask import Flask, render_template, redirect
from create_deck import Deck
from create_tables import Database

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
    while var.check is False:
        deck = Deck()
        var.deck_a, var.deck_b = deck.shuffle()
        #print(var.deck_a, var.deck_b)
        var.check = True
    if len(var.deck_a) < 1:
        return redirect("/")
    else:
        var.counter += 1
        value = next(var.deck_a, var.deck_b, var.counter)
        values, values2, counter = value
        name, attack, defense, types = values
        name2, attack2, defense2, types2 = values2
        return render_template('game_template.html', deck_a=var.deck_a, deck_b=var.deck_b, name=name, attack=attack, defense=defense, types=types, name2=name2, attack2=attack2, defense2=defense2, types2=types2, counter=counter)

def next(deck_a, deck_b, counter):
    database = Database()
    values = database.pokemonData(deck_a, counter)
    values2 = database.pokemonData(deck_b, counter)
    return values, values2, counter

@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == "__main__": app.run()
