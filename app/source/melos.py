from hashlib import sha256
import sqlite3
from connect import connect

def insert_melos(melos):
    con, cur = connect()
    cur.execute(f"INSERT INTO melos VALUES (?,?,?,?,?,?,?,?)", melos)
    con.commit()
    con.close()
