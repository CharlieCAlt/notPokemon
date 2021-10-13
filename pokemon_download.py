import requests


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
                type2 = ''
            for data in results:
                figure = data['stat']
                if figure['name'] == 'attack':
                    attack = data['base_stat']
                elif figure['name'] == 'defense':
                    defense = data['base_stat']
                else:
                    pass
            input_data = (pokenumber, name, artwork, attack, defense, type1, type2)
            pokenumber += 1
            database.createTables()
            database.addPokemon(input_data)
        else:
            pass

def typeURL(name):
    typeUrl = None
    r = requests.get("https://pokeapi.co/api/v2/type/")
    response = r.json()
    results = response["results"]
    for item in results:
        if item['name'] == name:
            typeUrl = item["url"]
    return typeUrl


def get_relations_types(typeUrl):
    r = requests.get(typeUrl)
    response = r.json()
    results = response["damage_relations"]
    double_damage_to_dict = results["double_damage_to"]
    half_damage_to_dict = results["half_damage_to"]
    no_damage_to_dict = results["no_damage_to"]
    double_damage_from_dict = results["double_damage_from"]
    half_damage_from_dict = results["half_damage_from"]
    no_damage_from_dict = results["no_damage_from"]
    double_damage_to = loop_dict(double_damage_to_dict)
    half_damage_to = loop_dict(half_damage_to_dict)
    no_damage_to = loop_dict(no_damage_to_dict)
    double_damage_from = loop_dict(double_damage_from_dict)
    half_damage_from = loop_dict(half_damage_from_dict)
    no_damage_from = loop_dict(no_damage_from_dict)
    return double_damage_to, half_damage_to, no_damage_to, double_damage_from, half_damage_from, no_damage_from

def loop_dict(dict):
    return_list = []
    for typeName in dict:
        return_list.append(typeName['name'])
    return return_list

