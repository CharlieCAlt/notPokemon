#game page scripts and functions
from flask import Flask, render_template, redirect
from create_deck import Deck

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
