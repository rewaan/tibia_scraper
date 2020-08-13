import sqlite3
from guild_memebers import *


chl = CharacterList()

class Databases:

    def __init__(self, guild=''):
        self.guild = guild

    @staticmethod
    def create_database(guild):
        connection = sqlite3.connect("{}.db".format(guild))
        crsr = connection.cursor()
        sql_command = """CREATE TABLE {} (  
        id INTEGER PRIMARY KEY,
        name VARCHAR(30)
        vocation VARCHAR(30)
        level INT);""".format(guild)
        crsr.execute(sql_command)
        for name in chl.name_list(guild):
            sql_command = """INSERT INTO {} ( VALUES (""".format(guild)
