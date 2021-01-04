from .melos import validate
from getpass import getpass

def login(*args):
    melos = input('Username: ')
    password = getpass()
    if validate(melos, password): 
        print('Logged in..')
        return melos
    print('Failed to log in..')
    return None
