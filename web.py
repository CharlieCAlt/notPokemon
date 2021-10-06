from flask import Flask, render_template, request
from create_tables import Database
import pokemon_download
import json

app = Flask(__name__)

database = Database()

button_count = 0

@app.route("/")
def pokedex():
    return render_template('pokedex2.html')


@app.route("/downloadPokemons")
def download_pokemons():
    global button_count
    print(button_count)
    if button_count % 2 == 0:
        database.delete_table()
        database.createTables()
        pokemon_download.getPokemon(database)
        alert = 'Do you want to override pokemon data?'
    else:
        alert = None
    button_count += 1
    names = database.returnNames()
    names_list = names.values.tolist()
    return render_template('pokedex2.html', names=names_list, alert=alert)

@app.route("/showPokemons")
def show_pokemons():
    names = database.returnNames()
    names_list = names.values.tolist()
    name = request.args.get('name')
    data = database.getAll(name)
    print(data)
    data_list = data.values.tolist()
    print(data_list)
    return render_template('pokedex2.html', names=names_list, name=data_list[0][1], art=data_list[0][2],
                           attack=data_list[0][3], defense=data_list[0][4], type=data_list[0][5])


if __name__ == "__main__": app.run()
