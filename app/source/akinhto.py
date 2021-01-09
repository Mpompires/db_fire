from .connect import connect
from .melos import get_melos_id

def does_akinhto_exist(akinhto_id):
    con, cur = connect()
    aggelies_found = cur.execute(f'SELECT count(akinhto_id)'
                                 f'  FROM akinhto '
                                 f'  WHERE akinhto_id == "{akinhto_id}"').fetchall()[0][0]
    con.close()
    if aggelies_found == 1:
        return True
    return False

def does_user_has_edit_privilege_aggelia(username, akinhto_id):
    pwlhths_id = get_melos_id(username)
    con, cur = connect()
    aggelies_found = cur.execute(f'SELECT count(akinhto_id) '
                                 f'   FROM akinhto '
                                 f'   WHERE akinhto_id == "{akinhto_id}" AND diaxhrizetai_pwlhths_id = "{pwlhths_id}"').fetchall()[0][0]
    con.close()
    if aggelies_found == 1:
        return True
    return False