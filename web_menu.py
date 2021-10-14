from deck import Deck
from flask import Flask, render_template, request, redirect
from database import Database
import pokemon_download

app = Flask(__name__)
database = Database()
button_count = 0


class Button:
    def __init__(self):
        database.createTables()
        self.deck_a = []
        self.deck_b = []
        self.counterA = 0
        self.counterB = 0
        deck = Deck()
        self.deck_a, self.deck_b = deck.shuffle()


var = Button()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/game")
def game():
    global var
    if len(var.deck_a) ==0:
        deck=Deck()
        var.deck_a, var.deck_b = deck.shuffle()
        return redirect("/")
    else:
        return render_template('game_template.html')


@app.route("/startA")
def startA():
    global var
    database = Database()
    values = database.pokemonData(var.deck_a, var.counterA)
    name, attack, defense, type1, type2 = values
    remaining_a = len(var.deck_a) - var.counterA
    if remaining_a == 0:
        var.counterA = 0
        remaining_a = len(var.deck_a) - var.counterA
    return render_template('cardStatsA.html', deck_a=var.deck_a, name=name, attack=attack, defense=defense, type1=type1,
                           type2=type2, counter1=var.counterA, remaining1=remaining_a)


@app.route("/startB")
def startB():
    global var
    database = Database()
    values = database.pokemonData(var.deck_b, var.counterB)
    name, attack, defense, type1, type2 = values
    remaining_b = len(var.deck_b) - var.counterB
    if remaining_b == 0:
        var.counterB = 0
        remaining_b = len(var.deck_b) - var.counterB
    return render_template('cardStatsB.html', deck_b=var.deck_b, name2=name, attack2=attack, defense2=defense,
                           typeB1=type1, typeB2=type2, counter2=var.counterB, remaining2=remaining_b)


@app.route("/cardStatsA")
def cardA():
    global var
    var.counterA += 1
    remaining_a = len(var.deck_a) - var.counterA
    if remaining_a == 0:
        var.counterA = 0
        remaining_a = len(var.deck_a) - var.counterA
    database = Database()
    values = database.pokemonData(var.deck_a, var.counterA)
    name, attack, defense, type1, type2 = values
    return render_template('cardStatsA.html', deck_a=var.deck_a, name=name, attack=attack, defense=defense, type1=type1,
                           type2=type2, counter1=var.counterA, remaining1=remaining_a)


@app.route("/cardStatsB")
def cardB():
    global var
    var.counterB += 1
    remaining_b = len(var.deck_b) - var.counterB
    if remaining_b == 0:
        var.counterB = 0
        remaining_b = len(var.deck_b) - var.counterB
    database = Database()
    values = database.pokemonData(var.deck_b, var.counterB)
    name, attack, defense, type1, type2 = values
    return render_template('cardStatsB.html', deck_b=var.deck_b, name2=name, attack2=attack, defense2=defense,
                           typeB1=type1, typeB2=type2, counter2=var.counterB, remaining2=remaining_b)


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
                           attack=data_list[0][3], defense=data_list[0][4], type1=data_list[0][5],
                           type2=data_list[0][6])

@app.route("/damageRelations")
def damage_relations():
    types = database.get_all_types()
    types_list = types.values.tolist()
    return render_template('damageRelations.html', types=types_list)

@app.route("/showDamageRelations")
def show_damage_relations():
    types = database.get_all_types()
    types_list = types.values.tolist()
    name = request.args.get('name')
    url = pokemon_download.typeURL(name)
    double_damage_to, half_damage_to, no_damage_to, double_damage_from, half_damage_from, no_damage_from = pokemon_download.get_relations_types(url)
    return render_template('damageRelations.html', double_damage_to=double_damage_to, half_damage_to=half_damage_to, no_damage_to=no_damage_to,
                           double_damage_from=double_damage_from, half_damage_from=half_damage_from, no_damage_from=no_damage_from, types=types_list, name=name)

if __name__ == "__main__": app.run()
