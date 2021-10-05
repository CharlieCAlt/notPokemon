import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('pokedex.db', check_same_thread=False)
except Error as e:
    print(e)
cursor = conn.cursor()

def addPokemon(input_data):
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
    cursor.execute(addition, input_data)
    conn.commit()

# This is a change