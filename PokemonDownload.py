import requests
import SQL_Data

# pokemon url https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151

def getPokemon():
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151')
    response = r.json()
    results = response['results']
    for pokemon in results:
        print (pokemon['name'])
        pokeName = pokemon['name']
        SQL_Data.addPokemon(pokeName)


def getPokeInfo():
    pass

getPokemon()
