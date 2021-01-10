from hashlib import sha256
import sqlite3
from .connect import connect
from .aggelia import search_aggelies_katoikia
from .printer import print_table, match_column_with_dictionary

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
        tmp = match_column_with_dictionary(tmp, {'enoikiazetai': 'Ενοικιάζεται', 'pwleitai': 'Πωλείται'}, 1)
        tmp = match_column_with_dictionary(tmp, {'polykatoikia': 'Πολυκατοικία', 'monokatoikia': 'Μονοκατοικία'}, 4)
        tmp = match_column_with_dictionary(tmp, {'autonomh': 'Αυτόνομη', 'kentrikh': 'Κεντρική'}, 5)
        print_table(tmp, ['ID αγγελίας', 'Πωλ./Εν.', 'Τιμή', ['Σημειώσεις',10], 'Τύπος κατοικίας', 'Σύστημα θέρμανσης', 'Μπάνια', 'Όροφος', 'Έτος κατασκευής'])
