from deck import Deck
from flask import Flask, render_template, request, redirect, url_for
from database import Database
import pokemon_download
from game_engine.game import Game

app = Flask(__name__)
button_count = 0

var = Game()
var.choose_attacker()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/game")
def game():
    global var
    if len(var.player_1.deck) == 0:
        deck = Deck()
        var.player_1.deck, var.player_2.deck = deck.shuffle()
        return redirect("/")
    else:
        database = Database()
        values = database.pokemonData(var.player_1.deck, var.player_1.counter)
        name, attack, defense, type1, type2 = values
        card = None
        if var.attacker.player_no == 1:
            card = cardB
        if var.attacker.player_no == 2:
            card = cardA
        turn = var.choose_attacker()
        if turn == var.player_1:
            option = 'Attacker'
        elif turn == var.player_2:
            option = 'Defender'
        print(option)
        return render_template('game_template.html', type1=type1, type2=type2, card=card, option=option)


@app.route("/cardBack")
def cardBack():
    return render_template("cardBack.html")


@app.route("/flipA")
def cardFlipA():
    global var
    database = Database()
    values = database.pokemonData(var.player_1.deck, var.player_1.counter)
    name, attack, defense, type1, type2 = values
    remaining_a = len(var.player_1.deck) - var.player_1.counter
    if remaining_a == 0:
        var.player_1.counter = 0
        remaining_a = len(var.player_1.deck) - var.player_1.counter
    return render_template('cardStatsA.html', deck_a=var.player_1.deck, name=name, attack=attack, defense=defense,
                           type1=type1, type2=type2, counter1=var.player_1.counter, remaining1=remaining_a)


@app.route("/flipB")
def cardFlipB():
    global var
    database = Database()
    values = database.pokemonData(var.player_2.deck, var.player_2.counter)
    name, attack, defense, type1, type2 = values
    remaining_b = len(var.player_2.deck) - var.player_2.counter
    if remaining_b == 0:
        var.player_2.counter = 0
        remaining_b = len(var.player_2.deck) - var.player_2.counter
    return render_template('cardStatsB.html', deck_b=var.player_2.deck, name2=name, attack2=attack, defense2=defense,
                           typeB1=type1, typeB2=type2, counter2=var.player_2.counter, remaining2=remaining_b)
        return render_template('game_template.html', type1=type1, type2=type2)

@app.route("/turnChoice")
def turn_choice():
    turn=var.choose_attacker()
    if turn == var.player_1:
        option = 'Attacker'
    elif turn == var.player_2:
        option = 'Defender'
    return render_template('turn.html', option=option)


@app.route("/startA")
def startA():
    global var
    database = Database()
    values = database.pokemonData(var.player_1.deck, var.player_1.counter)
    name, attack, defense, type1, type2 = values
    remaining_a = len(var.player_1.deck) - var.player_1.counter
    if remaining_a == 0:
        var.player_1.counter = 0
        remaining_a = len(var.player_1.deck) - var.player_1.counter
    if var.attacker.player_no == 1:
        return render_template('cardStatsA.html', deck_a=var.player_1.deck, name=name, attack=attack, defense=defense,
                               type1=type1, type2=type2, counter1=var.player_1.counter, remaining1=remaining_a)
    if var.defender.player_no == 1:
        return render_template('cardBack.html')


@app.route("/startB")
def startB():
    global var
    database = Database()
    values = database.pokemonData(var.player_2.deck, var.player_2.counter)
    name, attack, defense, type1, type2 = values
    remaining_b = len(var.player_2.deck) - var.player_2.counter
    if remaining_b == 0:
        var.player_2.counter = 0
        remaining_b = len(var.player_2.deck) - var.player_2.counter
    if var.attacker.player_no == 2:
        return render_template('cardStatsB.html', deck_b=var.player_2.deck, name2=name, attack2=attack,
                               defense2=defense, typeB1=type1, typeB2=type2, counter2=var.player_2.counter,
                               remaining2=remaining_b)
    if var.defender.player_no == 2:
        return render_template('cardBack.html')


@app.route("/cardStatsA")
def cardA():
    global var
    var.player_1.counter += 1
    remaining_a = len(var.player_1.deck) - var.player_1.counter
    if remaining_a == 0:
        var.player_1.counter = 0
        remaining_a = len(var.player_1.deck) - var.player_1.counter
    database = Database()
    values = database.pokemonData(var.player_1.deck, var.player_1.counter)
    name, attack, defense, type1, type2 = values
    if var.attacker.player_no == 1:
        return render_template('cardStatsA.html', deck_a=var.player_1.deck, name=name, attack=attack, defense=defense,
                               type1=type1, type2=type2, counter1=var.player_1.counter, remaining1=remaining_a)
    if var.defender.player_no == 1:
        return render_template('cardBack.html')


@app.route("/cardStatsB")
def cardB():
    global var
    var.player_2.counter += 1
    remaining_b = len(var.player_2.deck) - var.player_2.counter
    if remaining_b == 0:
        var.player_2.counter = 0
        remaining_b = len(var.player_2.deck) - var.player_2.counter
    database = Database()
    values = database.pokemonData(var.player_2.deck, var.player_2.counter)
    name, attack, defense, type1, type2 = values
    if var.attacker.player_no == 2:
        return render_template('cardStatsB.html', deck_b=var.player_2.deck, name2=name, attack2=attack,
                               defense2=defense, typeB1=type1, typeB2=type2, counter2=var.player_2.counter,
                               remaining2=remaining_b)
    if var.defender.player_no == 2:
        return render_template('cardBack.html')


@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/initial_pokemon_type")
def find_initial_type():
    database = Database()
    values = database.pokemonData(var.player_1.deck, var.player_1.counter)
    name, attack, defense, type1, type2 = values
    return render_template('initial_pokemon_type.html' , initial_pokemon_type=type1)

@app.route("/second_pokemon_type")
def find_second_type():
    database = Database()
    values = database.pokemonData(var.player_1.deck, var.player_1.counter)
    name, attack, defense, type1, type2 = values
    return render_template('second_pokemon_type.html' , second_pokemon_type=type2)


@app.route("/pokedex")
def display_pokedex():
    return render_template('pokedex.html')


@app.route("/downloadPokemons")
def download_pokemons():
    database = Database()
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
    deck = Deck()
    deck_a, deck_b = deck.shuffle()
    var.player_1.deck = deck_a
    var.player_2.deck = deck_b
    return render_template('pokedex.html', names=names_list, alert=alert)

@app.route("/attackPokemon")
def attack_pokemons():
    choice=request.args.get('types')
    print(choice)
    return render_template('Game_Rules.html')


@app.route("/showPokemons")
def show_pokemons():
    database = Database()
    names = database.returnNames()
    names_list = names.values.tolist()
    name = request.args.get('name')
    data = database.getAll(name)
    data_list = data.values.tolist()
    return render_template('card.html', names=names_list, name=data_list[0][1], art=data_list[0][2],
                           attack=data_list[0][3], defense=data_list[0][4], type1=data_list[0][5],
                           type2=data_list[0][6])

@app.route("/rules")
def game_rules():
    return render_template('Game_Rules.html')




if __name__ == "__main__": app.run()
