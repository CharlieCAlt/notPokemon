from flask import Flask, render_template, request
from create_tables import Database
import pokemon_download

app = Flask(__name__)

database = Database()

@app.route("/")
def pokedex():
    return render_template('pokedex2.html')


@app.route("/downloadPokemons")
def download_pokemons():
    database.CreateTables()
    pokemon_download.getPokemon(database)
    return render_template('pokedex2.html')
    

if __name__ == "__main__": app.run()
