import sqlite3
from sqlite3 import Error

def create_Connection():
    
    try:
        conn = sqlite3.connect('db/books_db.db')
        return conn
    except Error as e:
        print('Error connecting to database: ' + str(e)) 

    