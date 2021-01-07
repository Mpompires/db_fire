from hashlib import sha256
import sqlite3
from .connect import connect
from .aggelia import search_aggelies_katoikia
from .printer import print_table

def search(*args):
    typ = input('-- 1 (katoikia) or 2 (epaggelmatikos xwros) or 3 (gh): ')
    if typ == '1':
        min_price = input('-- Min price: ')
        max_price = input('-- Max price: ')
        kat_type = input('-- 1 (monokatoikia) or 2 (polykatoikia): ') 
        heating_system = input('-- 1 (autonomh) or 2 (kentrikh): ')
        min_bathrooms = input('-- Min bathrooms: ')
        max_bathrooms = input('-- Max bathrooms: ')
        min_construction_year = input('-- Contructed after: ')
        max_construction_year = input('-- Constructed before: ')
        tmp = search_aggelies_katoikia(kat_type, min_price, max_price, heating_system, min_bathrooms, max_bathrooms, min_construction_year, max_construction_year)
        print_table(tmp, ["akinito_id", "aggelia_type", "price", ["aggelia_text",3], "katoikia_type", "heating_system", "bathrooms", "floors", "construction_year"])
