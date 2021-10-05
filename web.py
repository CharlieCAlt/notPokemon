from flask import Flask, render_template, request
from create_tables import Database
import pokemon_download

app = Flask(__name__)

database = Database()

button_count = 0

@app.route("/")
def pokedex():
    return render_template('pokedex2.html')


@app.route("/downloadPokemons")
def download_pokemons():
    global button_count
    if button_count == 0:
        database.createTables()
        pokemon_download.getPokemon(database)
    else:
        pass
        # Add functionality which shows a message if the user click download data
    button_count += 1
    names = database.returnNames()
    names_list = names.values.tolist()
    return render_template('pokedex2.html', names=names_list)

def show_pokemons():
    names = database.returnNames()
    names_list = names.values.tolist()
    return render_template('pokedex2.html', names=names_list)
    

if __name__ == "__main__": app.run()
