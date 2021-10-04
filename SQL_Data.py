import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('Pokedex.db', check_same_thread=False)
except Error as e:
    print(e)
cursor = conn.cursor()

def addPokemon(pokeName):
    addition = f"""
    INSERT INTO pokemon (Name)
    VALUES(
    ?
    )
    """
    cursor.execute(addition, pokeName)
    conn.commit()
