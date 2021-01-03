import sqlite3

def connect():
    con = sqlite3.connect("db.db")
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    return (con, cur)
