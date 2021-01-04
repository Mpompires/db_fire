from source.signup import signup
from source.search import search
from source.login import login

current_user = None

def logout():
    return None

options = {
    's': signup,
    'lin': login,
    'lout': logout,
    's': search
}

def check(option):
    if option not in options:
        print('Invalid option..')
        return False
    if option == 's':
        if current_user is not None:
            print('Cannot signup while logged in..')
            return False
    elif option == 'lin':
        if current_user is not None:
            print('Already logged in..')
            return False
    elif option == 'lout':
        if current_user is None:
            print('Not logged in..')
            return False
    return True

while True:
    option = input(f'{current_user}> ')
    if check(option): current_user = options[option]()
