from hashlib import sha256
import sqlite3
from .connect import connect

def search():
    print('-- Select 1 (katoikia) or 2 (epaggelmatikos xwros) or 3 (gh)')
    typ = input('-- Type: ')
    if typ == '1':
        kat_type = input('-- 1 (monokatoikia) or 2 (polykatoikia): ') 
        heating_system = input('-- 1 (autonomh) or 2 (kentrikh): ')
        min_bathrooms = input('-- Min bathrooms: ')
        max_bathrooms = input('-- Max bathrooms: ')
        min_construction_year = int(input('-- Contructed after: '))
        max_construction_year = int(input('-- Constructed before: '))

    con, cur = connect()
    con.commit()
    con.close()
