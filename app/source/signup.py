from .melos import insert_melos
import hashlib

def signup():
    username = input('Username: ')
    password = hashlib.sha256(input('Password: ').encode('utf-8')).digest()
    email = input('Email: ')
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    is_endiaferomenos = 1
    is_pwlhths = 0
    row = (None, username, password, email, first_name, last_name, is_endiaferomenos, is_pwlhths)
    insert_melos(row)
