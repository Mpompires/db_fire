from .connect import connect
from .printer import print_table,print_row

def _does_username_exist(username):
    con, cur = connect()
    meloi_found = cur.execute(f'SELECT count(melos_id) FROM melos WHERE username == "{username}"').fetchall()[0][0]
    con.close()
    if meloi_found == 1:
        return True
    return False


def _get_melos_id(username):
    con, cur = connect()
    melos_id = cur.execute(f'SELECT melos_id FROM melos WHERE username == "{username}"').fetchall()[0][0]
    con.close()
    return melos_id


def mod_list_akinhta_pwlhth(*args):
    username_in_question = input("Username of pwlhth (just press ENTER to list all akinhta): ")
    if len(username_in_question) == 0:
        con, cur = connect()
        result_table = cur.execute(f'SELECT akinito_id, surface_area, area, area_coords, description, extra, username'
                                   f'   FROM akinhto JOIN melos ON diaxhrizetai_pwlhths_id = melos_id').fetchall()
        print_table(result_table,
                    ['ID ακινήτου', 'Εμβαδόν', 'Περιοχή', 'Συντεταγμένες', ['Περιγραφή', 25], ['Επιπρόσθετες πληροφορίες', 25], 'Username'])
        con.close()
    elif _does_username_exist(username_in_question):
        melos_id = _get_melos_id(username_in_question)
        con, cur = connect()
        result_table = cur.execute(f'SELECT akinito_id, surface_area, area, area_coords, description, extra'
                                   f'   FROM akinhto'
                                   f'   WHERE diaxhrizetai_pwlhths_id == {melos_id}').fetchall()
        print_table(result_table,
                    ['ID ακινήτου', 'Εμβαδόν', 'Περιοχή', 'Συντεταγμένες', ['Περιγραφή', 25], ['Επιπρόσθετες πληροφορίες', 25]])
        con.close()
    else:
        print("No such user..")


def mod_list_akinhta_idiwkthth(*args):
    first_name = input("First name of idiwkthth: ")
    last_name = input("Last name of idiwkthth: ")

    queue = (f'SELECT akinito_id, surface_area, area, area_coords, description, extra, username'
             f'   FROM akinhto JOIN melos ON diaxhrizetai_pwlhths_id = melos_id'
             f'   WHERE TRUE ')
    if(len(first_name) != 0):
        queue += (f'AND akinhto.first_name_idiokthth == "{first_name}"')
    if (len(last_name) != 0):
        queue += (f'AND akinhto.last_name_idiokthth == "{last_name}"')

    con, cur = connect()
    result_table = cur.execute(queue).fetchall()
    con.close()

    print_table(result_table,
                ['ID ακινήτου', 'Εμβαδόν', 'Περιοχή', 'Συντεταγμένες', ['Περιγραφή', 25], ['Επιπρόσθετες πληροφορίες', 25], 'Username Πωλητή'])

