import sqlite3, csv

con = sqlite3.connect("db.db")
con.execute("PRAGMA foreign_keys = 1")
cur = con.cursor()

def enter_data_for(entity):
    data = open(f"data/{entity[0]}.csv")
    rows = csv.reader(data)
    cols = '(?' + ',?' * (entity[1]-1) + ')'
    cur.executemany(f"INSERT INTO {entity[0]} VALUES {cols}", rows)

entities = [
    ("akinhto", 6),
    ("a_katoikia", 8),
    ("a_epaggelmatikos_xwros", 5),
    ("a_gh", 3)
]

for entity in entities:
    enter_data_for(entity)

con.commit()
con.close()
