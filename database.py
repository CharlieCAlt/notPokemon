import pandas as pd
import sqlite3
from sqlite3 import Error

class Database:

    def __init__(self):
        try:
            self.conn = sqlite3.connect('pokedex.db', check_same_thread=False)
        except Error as e:
            print(e)
            raise e
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def createTables(self):
        createPokedex = '''
        CREATE TABLE IF NOT EXISTS Pokedex (
        ID INT PRIMARY KEY,
        Name VARCHAR(20),
        Artwork VARCHAR(100),
        Attack INT,
        Defense INT,
        Types VARCHAR(20),
        UNIQUE(ID, Name)
        )'''
        self.cursor.execute(createPokedex)
        self.conn.commit()

    def addPokemon(self, input_data):
        addition = f"""
        INSERT INTO Pokedex (ID, Name, Artwork, Attack, Defense, Types)
        VALUES(
        ?,
        ?,
        ?,
        ?,
        ?,
        ?
        )
        """
        self.cursor.execute(addition, input_data)
        self.conn.commit()

    def pokemonData(self, deck, counter):
        pokemon_find = deck[counter]
        find_pokemon = """
            SELECT Name, Attack, Defense, Types
            FROM Pokedex
            WHERE ID=?
                    """
        self.cursor.execute(find_pokemon, (pokemon_find,))
        data = self.cursor.fetchone()
        return data

    def returnNames(self):
        names = f"""
        SELECT Name 
        FROM Pokedex
        """
        df = pd.read_sql_query(names, self.conn)
        return df

    def getArt(self, name):
        art = f"""
        SELECT Artwork
        FROM Pokedex
        WHERE Name = ? """
        df = pd.read_sql_query(art, self.conn, params=(name,))
        return df

    def getAll(self, name):
        data = f"""
        SELECT * 
        FROM Pokedex 
        WHERE name = ? """
        df = pd.read_sql_query(data, self.conn, params=(name,))
        return df

    def delete_table(self):
        query = f"""DROP TABLE Pokedex"""
        self.cursor.execute(query)
        self.conn.commit()

