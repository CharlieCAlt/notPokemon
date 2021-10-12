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


def damageModifier(attackerType, defenseType1, defenseType2):
    url = typeURL(attackerType)
    defenseType =[defenseType1, defenseType2]
    modifier = calculateModifier(url, defenseType)
    modifier /= 10
    return modifier


def typeURL(attackerType):
    typeUrl = None
    r = requests.get("https://pokeapi.co/api/v2/type/")
    response = r.json()
    results = response["results"]
    for type in results:
        typeName = type["name"]
        if typeName == attackerType:
            typeUrl = type["url"]
    return typeUrl


def calculateModifier(typeUrl, defenseType):
    dmgModifier = int(10)
    r = requests.get(typeUrl)
    response = r.json()
    results = response["damage_relations"]
    doubleDamage = results["double_damage_to"]
    halfDamage = results["half_damage_to"]
    noDamage = results["no_damage_to"]
    for dType in defenseType:
        for typeName in doubleDamage:
            if dType in typeName.values():
                dmgModifier *= 2
        for typeName in halfDamage:
            if dType in typeName.values():
                dmgModifier *= 0.5
        for typeName in noDamage:
            if dType in typeName.values():
                dmgModifier *= 0
    return dmgModifier
