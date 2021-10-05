import requests
import SQL_Data

class Pokemon:
    """ A Pokemon with Name, Artwork, Attack, Defense and Type stored for database input"""

    def __init__(self, name, artwork, attack, defense, types):
        self.__name=name
        self.__artwork = artwork
        self.__attack = attack
        self.__defense = defense
        self.__types = types

def getPokemon():
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151')
    response = r.json()
    results = response['results']
    pokenumber = 1
    for pokemon in results:
        print('------------')
        print(pokemon['name'])
        Name = pokemon['name']
        if 0 < pokenumber < 152:
            stats = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokenumber}/")
            response = stats.json()
            results = response['stats']
            pictures = response['sprites']
            Artwork = pictures['front_default']
            type_data = response['types']
            breed = type_data[0]
            type = breed['type']
            Type1 = type['name']
            try:
                new_breed = type_data[1]
                new_type = new_breed['type']
                Type2 = new_type['name']
                print(Type1, Type2)
                Types = (Type1, Type2)
            except IndexError:
                print(Type1)
                Types = Type1
            print(Artwork)
            for data in results:
                figure = data['stat']
                if figure['name'] == 'attack':
                    print(figure['name'], data['base_stat'])
                    Attack = (data['base_stat'])
                if figure['name'] == 'defense':
                    print(figure['name'], data['base_stat'])
                    Defense = data['base_stat']
                else:
                   pass
            bob = Pokemon(Name, Artwork, Attack, Defense, Types)
            input_data = (pokenumber, Name, Artwork, Attack, Defense, str(Types))
            print(input_data)
            pokenumber += 1
        else:
            pass
        SQL_Data.addPokemon(input_data)

if __name__ == '__main__':
    getPokemon()