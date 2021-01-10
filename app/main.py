from source.connect import create_db_if_not_exist
from source.signup import signup
from source.search import search
from source.login import login
from source.aggelia import about_aggelia
from source.akinhto import create_akinhto, about_akinhto_of_pwlhth
from source.melos import is_mod, is_pwlhths, is_endiaferomenos
from source.endiaferomenos import signup_endiaferomenos, endiaferetai_for_aggelia
from source.pwlhths import list_my_aggelies, list_my_akinhta
from source.signup_pwlhths import signup_pwlhths
from source.mod_tools import add_root_if_not_exist, mod_sign_as, mod_appoint_new_mod, mod_list_akinhta_idiokthth, mod_list_mesitika_grafeia, mod_list_pwlhtes
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
    'sine': signup_endiaferomenos,
    'lsag': list_my_aggelies,
    'lsak': list_my_akinhta,
    'crak': create_akinhto,
    'crag': create_aggelia,
    'abak': about_akinhto_of_pwlhth,
    'abag': about_aggelia,
    'enag': endiaferetai_for_aggelia,
    'mod_sign_as': mod_sign_as,
    'mod_appoint_new_mod': mod_appoint_new_mod,
    'mod_list_akinhta_idiokthth': mod_list_akinhta_idiokthth,
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
            return False
    elif option == 'sine':
        if current_user is None:
            print('Not logged in..')
            return False
        if is_endiaferomenos(current_user):
            print('Already endiaferomenos')
            return False
    elif option == 'abak':
        if current_user is None:
            print('Not logged in..')
            return False
        elif not is_pwlhths(current_user) and not is_mod(current_user):
            print('You need to sign up as pwlhths or mod..')
            return False
    elif option == 'enag':
        if current_user is None:
            print('Not logged in..')
            return False
        elif not is_endiaferomenos(current_user):
            print('You need to become endiaferomenos..')
            return False
    elif option == 'crak' \
       or option == 'crag' \
       or option == 'lsag' \
       or option == 'lsak':
        if current_user is None:
            print('Not logged in..')
            return False
        elif not is_pwlhths(current_user):
            print('You need to sign up as pwlhths..')
            return False
    elif option == 'mod_sign_as' \
      or option == 'mod_appoint_new_mod'\
      or option == 'mod_list_akinhta_idiokthth' \
      or option == 'mod_list_mesitika_grafeia' \
      or option == 'mod_list_pwlhtes':
        if current_user is None:
            print('Not logged in..')
            return False
        if not is_mod(current_user):
            print('No permission :/')
            return False
    return True

create_db_if_not_exist()
add_root_if_not_exist()

while True:
    option = input(f'{current_user}> ')
    if option == 'quit':
        quit()
    elif check(option):
        return_user = options[option](current_user)
        if return_user is not None:
            current_user = return_user

