from flask import Flask, render_template, request
from create_deck import Deck

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/game")
def game():
    Deck.shuffle()
    return render_template('game_template.html')

if __name__ == "__main__": app.run()
