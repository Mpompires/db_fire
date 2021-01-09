from source.signup import signup
from source.search import search
from source.login import login
from source.akinhto import create_akinhto, about_akinhto_of_pwlhth
from source.melos import is_mod, is_pwlhths
from source.pwlhths import list_my_aggelies, list_my_akinhta
from source.signup_pwlhths import signup_pwlhths
from source.mod_tools import mod_sign_as, mod_list_akinhta_idiwkthth, mod_list_mesitika_grafeia, mod_list_pwlhtes
from source.aggelia import create_aggelia

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
    'lsag': list_my_aggelies,
    'lsak': list_my_akinhta,
    'crak': create_akinhto,
    'abak': about_akinhto_of_pwlhth,
    'mod_sign_as': mod_sign_as,
    'mod_list_akinhta_idiwkthth': mod_list_akinhta_idiwkthth,
    'mod_list_mesitika_grafeia' : mod_list_mesitika_grafeia,
    'mod_list_pwlhtes': mod_list_pwlhtes,
    'crag': create_aggelia
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
            return False
    elif option == 'abak':
        if current_user is None:
            print('Not logged in..')
            return False
        elif not is_pwlhths(current_user) and not is_mod(current_user):
            print('You need to sign up as pwlhths or mod..')
            return False
    elif option == 'crak' \
       or option == 'lsag' \
       or option == 'lsak':
        if current_user is None:
            print('Not logged in..')
            return False
        elif not is_pwlhths(current_user):
            print('You need to sign up as pwlhths..')
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
    elif option == 'crag':
        if current_user is None:
            print('Not logged in..')
            return False
        if not is_pwlhths(current_user):
            print('You need to sign up as pwlhths..')
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

