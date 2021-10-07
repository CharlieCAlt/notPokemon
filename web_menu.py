from flask import Flask, render_template, redirect
from create_deck import Deck
import game_page

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/game")
def game():
    deck=Deck()
    deck_a, deck_b = deck.shuffle()
    values = game_page.pokemon_data(deck_a)
    name, attack, defense, types = values
    print(values)
    if len(deck_a) < 1:
        return redirect("/")
    else:
        return render_template('game_template.html', deck_a = deck_a, deck_b=deck_b, name=name, attack=attack, defense=defense, types=types)

@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == "__main__": app.run()
