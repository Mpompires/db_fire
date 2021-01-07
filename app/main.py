from source.signup import signup
from source.search import search
from source.login import login
from source.melos import is_mod, is_pwlhths
from source.signup_pwlhths import signup_pwlhths
from source.mod_tools import mod_sign_as, mod_list_akinhta_idiwkthth

current_user = None


def logout(*args):      # dirty stuff
    global current_user
    current_user = None

options = {
    'sin': signup,
    'lin': login,
    'lout': logout,
    's': search,
    'sinp': signup_pwlhths,
    'mod_sign_as': mod_sign_as,
    'mod_list_akinhta_idiwkthth': mod_list_akinhta_idiwkthth
}

def check(option):
    if option not in options:
        print('Invalid option..')
        return False

    if option == 'sin':
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
    elif option == 'sinp':
        if current_user is None:
            print('Not logged in..')
            return False
        if is_pwlhths(current_user):
            print('Already pwlhths')
    elif option == 'mod_sign_as' or option == 'mod_list_akinhta_idiwkthth':
        if current_user is None:
            print('Not logged in..')
            return False
        if not is_mod(current_user):
            print('No permission :/')
            return False
    return True


while True:
    option = input(f'{current_user}> ')
    if option == 'quit':
        quit()
    elif check(option):
        return_user = options[option](current_user)
        if return_user is not None:
            current_user = return_user

