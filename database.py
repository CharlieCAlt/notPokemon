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

    def CreateTables(self):
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
