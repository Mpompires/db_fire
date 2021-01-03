from hashlib import sha256
import sqlite3

def insert_melos(melos):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO melos VALUES (?,?,?,?,?,?,?,?)", melos)
    con.commit()
    con.close()
