import os
import sqlite3
from .conn import getDBConnection, DB_FILE
from .queryrunner import QueryRunner

CREATE_TODO = 'CREATE TABLE todo(id integer primary key autoincrement not null, name text not null, description text, due date not null)'

def initDB():
    is_new = not os.path.exists(DB_FILE)
    conn = getDBConnection()
    query = QueryRunner(conn)
    if is_new:
        query.runDDL(CREATE_TODO)   
    conn.close()