import csv
from source.connect import connect
from hashlib import sha256

con, cur = connect()

def enter_data_for(entity):
    data = open(f"data/{entity[0]}.csv")
    rows = csv.reader(data)
    if entity[0] == "melos":
        rows = [row for row in rows]
        for row in rows:
            row[2] = sha256(row[2].encode('utf-8')).digest()
            cols = '(?' + ',?' * (entity[1]-1) + ')'
            cur.execute(f"INSERT INTO melos VALUES {cols}", row)
    else:
        cols = '(?' + ',?' * (entity[1]-1) + ')'
        for row in rows:
            cur.execute(f"INSERT INTO {entity[0]} VALUES {cols}", row)

entities = [
    ("melos", 9),
    ("mesitiko_grafeio", 3),
    ("m_pwlhths",3),
    ("akinhto", 10),
    ("a_katoikia", 8),
    ("a_epaggelmatikos_xwros", 5),
    ("a_gh", 3),
    ("aggelia", 11)
]

for entity in entities:
    enter_data_for(entity)

con.commit()
con.close()
