from create_tables import Database
import pokemon_download

def main():
    database = Database()
    database.createTables()
    pokemon_download.getPokemon(database)

if __name__ == '__main__':
    main()