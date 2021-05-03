import sqlite3
DB_FILE = './db/todo.db'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def getDBConnection():    
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = dict_factory
    return conn