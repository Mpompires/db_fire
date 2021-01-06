from .connect import connect

def is_mod(username):
    con, cur = connect()
    is_mod_int = cur.execute(f'SELECT is_mod FROM melos WHERE username == "{username}"').fetchall()[0][0]
    con.close()
    if is_mod_int == 1:
        return True
    return False

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
        result_table = cur.execute(f'SELECT * FROM akinhto').fetchall()
        con.close()
    elif _does_username_exist(username_in_question):
        melos_id = _get_melos_id(username_in_question)
        con, cur = connect()
        result_table = cur.execute(f'SELECT * FROM akinhto WHERE diaxhrizetai_pwlhths_id == {melos_id}').fetchall()
        con.close()
    else:
        print("No such user..")
        return None

    for row in result_table:
        for col in row:
            print(str(col) + ' ', end ='' )
        print('')

