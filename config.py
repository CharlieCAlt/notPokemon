import os

if os.getcwd().endswith('tests'):
    DATABASE = '../pokedex.db'
else:
    DATABASE = 'pokedex.db'