from source.signup import signup
from source.search import search
from source.login import login
from source.melos import is_mod, is_pwlhths
from source.pwlhths import list_my_aggelies, list_my_akinhta
from source.signup_pwlhths import signup_pwlhths
from source.mod_tools import mod_sign_as, mod_list_akinhta_idiwkthth, mod_list_mesitika_grafeia, mod_list_pwlhtes

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
    'list_my_aggelies': list_my_aggelies,
    'list_my_akinhta': list_my_akinhta,
    'mod_sign_as': mod_sign_as,
    'mod_list_akinhta_idiwkthth': mod_list_akinhta_idiwkthth,
    'mod_list_mesitika_grafeia' : mod_list_mesitika_grafeia,
    'mod_list_pwlhtes': mod_list_pwlhtes
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
    elif option == 'list_my_aggelies' \
       or option == 'list_my_akinhta':
        if current_user is None:
            print('Not logged in..')
            return False
        if not is_pwlhths(current_user):
            print('You are not pwlhths')
            return False
    elif option == 'mod_sign_as' \
      or option == 'mod_list_akinhta_idiwkthth' \
      or option == 'mod_list_mesitika_grafeia' \
      or option == 'mod_list_pwlhtes':
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

