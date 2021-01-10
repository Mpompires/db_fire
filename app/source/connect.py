import sqlite3

db_path = 'db.db'
db_source_path = '../db.sql'

def create_db_if_not_exist():
    try:
        con = sqlite3.connect(f'file:{db_path}?mode=rw', uri=True)
    except sqlite3.OperationalError:
        print("No db found, creating...")
        con = sqlite3.connect(f'file:{db_path}?mode=rwc', uri=True)
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()

        with open(db_source_path, 'r') as db_source_file:
            db_source = db_source_file.read()

        cur.executescript(db_source)
        con.commit()
    con.close()

def connect():
    con = sqlite3.connect(f'file:{db_path}?mode=rw', uri=True)
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()
    return (con, cur)
