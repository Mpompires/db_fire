from hashlib import sha256
import sqlite3
from .connect import connect

def insert_melos(melos):
    con, cur = connect()
    cur.execute(f"INSERT INTO melos VALUES (?,?,?,?,?,?,?,?)", melos)
    con.commit()
    con.close()

def validate(melos, password):
    con, cur = connect()
    melos = cur.execute(f'SELECT password FROM melos WHERE username == "{melos}"').fetchall()
    if melos and melos[0][0] == sha256(password.encode('utf-8')).digest():
        return True
    return False
