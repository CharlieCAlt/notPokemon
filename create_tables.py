from sql import *


class CreateTables:
    createPokedex = '''
    CREATE TABLE IF NOT EXISTS Pokedex (
    ID INT PRIMARY KEY,
    Name VARCHAR(20),
    Artwork VARCHAR(100),
    Attack INT,
    Defense INT,
    Type VARCHAR(20),
    UNIQUE(ID, Name)
    )'''
    cursor.execute(createPokedex)
    conn.commit()

test = CreateTables