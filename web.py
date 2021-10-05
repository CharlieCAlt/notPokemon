from flask import Flask, render_template, request
from create_tables import CreateTables

app = Flask(__name__)

database = CreateTables()

@app.route("/")
def pokedex():
    return render_template('pokedex2.html')

'''

@app.route("/displayPokemons")
def display_pokemons():
    # get pokemons from database
    getPokemon()
    pokemons = get_pokemons(book_title)
    pokemon_list = pokemons.values.tolist()
    return render_template('info.html', pokemons=pokemon_list)
    
'''

if __name__ == "__main__": app.run()
