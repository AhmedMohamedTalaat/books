import sqlite3
from sqlite3 import Error


class DataBase:
    @staticmethod
    def create_connection(path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            cursor = connection.cursor()
            # create table if not exist
            table_if_not_exist = 'create table if not exists books (id INTEGER PRIMARY KEY,' \
                                 'title varchar(255),' \
                                 'author varchar(225),' \
                                 'description  varchar(225));'
            cursor.execute(table_if_not_exist)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

