import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('pokedex.db', check_same_thread=False)
except Error as e:
    print(e)
cursor = conn.cursor()
