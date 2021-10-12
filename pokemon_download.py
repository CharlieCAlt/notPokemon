import requests
import pprint

class Pokemon:
    """ A Pokemon with Name, Artwork, Attack, Defense and Type stored for database input"""

    def __init__(self, name, artwork, attack, defense, types):
        self.__name = name
        self.__artwork = artwork
        self.__attack = attack
        self.__defense = defense
        self.__types = types

def getPokemon(database):
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151')
    response = r.json()
    results = response['results']
    pokenumber = 1
    for pokemon in results:
        name = pokemon['name']
        if 0 < pokenumber < 152:
            stats = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokenumber}/")
            response = stats.json()
            results = response['stats']
            pictures = response['sprites']
            artwork = pictures['front_default']
            type_data = response['types']
            breed = type_data[0]
            type = breed['type']
            type1 = type['name']
            attack = 0
            defense = 0
            try:
                new_breed = type_data[1]
                new_type = new_breed['type']
                type2 = new_type['name']
                types = (type1, type2)
            except IndexError:
                types = type1
            for data in results:
                figure = data['stat']
                if figure['name'] == 'attack':
                    attack = data['base_stat']
                elif figure['name'] == 'defense':
                    defense = data['base_stat']
                else:
                    pass
            input_data = (pokenumber, name, artwork, attack, defense, str(types))
            pokenumber += 1
            database.addPokemon(input_data)
        else:
            pass

def typeModifier(attacker, defender):
    if "normal" in attacker:
        rock = 0.5
        ghost = 0
        steel = 0.5
    elif "fighting" in attacker:
        normal = 2
        ice = 2
        poison = 0.5
        flying = 0.5
        psychic = 0.5
        bug = 0.5
        rock = 2
        ghost = 0
        dark = 2
        steel = 2
        fairy = 0.5
    elif "flying" in attacker:
        electric = 0.5
        grass = 2
        fighting = 2
        bug = 2
        rock = 0.5
        steel = 0.5
    elif "poison" in attacker:
        grass = 2
        fairy = 2
        poison = 0.5
        ground = 0.5
        rock = 0.5
        ghost = 0.5
        steel = 0
    elif "ground" in attacker:
        poison = 2
        rock = 2
        steel = 2
        fire = 2
        electric = 2
        bug = 0.5
        grass = 0.5
        flying = 0
