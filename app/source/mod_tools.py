from .connect import connect
from .uwu_print import uwu_print

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

def mod_list_akinhta(*args):
    username_in_question = input("Username of pwlhth (just press ENTER to list all akinhta): ")
    if len(username_in_question) == 0:
        con, cur = connect()
        result_table = cur.execute(f'SELECT akinito_id, surface_area, area, area_coords, description, extra, username'
                                   f'   FROM akinhto JOIN melos ON diaxhrizetai_pwlhths_id = melos_id').fetchall()
        uwu_print(result_table, ['ID ακινήτου', 'Εμβαδόν', 'Περιοχή', 'Συντεταγμένες', 'Περιγραφή', 'Επιπρόσθετες πληροφορίες', 'Username'])
        con.close()
    elif _does_username_exist(username_in_question):
        melos_id = _get_melos_id(username_in_question)
        con, cur = connect()
        result_table = cur.execute(f'SELECT akinito_id, surface_area, area, area_coords, description, extra '
                                   f'   FROM akinhto'
                                   f'   WHERE diaxhrizetai_pwlhths_id == {melos_id}').fetchall()
        uwu_print(result_table, ['ID ακινήτου', 'Εμβαδόν', 'Περιοχή', 'Συντεταγμένες', 'Περιγραφή', 'Επιπρόσθετες πληροφορίες'])
        con.close()
    else:
        print("No such user..")



