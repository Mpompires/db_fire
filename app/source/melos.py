from hashlib import sha256
from .connect import connect

def insert_melos(melos):
    con, cur = connect()
    try:
        cur.execute(f"INSERT INTO melos VALUES (?,?,?,?,?,?,?,?,?)", melos)
        con.commit()
        con.close()
        print('Succesfully signed up..')
    except:
        print('Username already used..')

def validate(melos, password):
    con, cur = connect()
    melos = cur.execute(f'SELECT password FROM melos WHERE username == "{melos}"').fetchall()
    con.close()
    if melos and melos[0][0] == sha256(password.encode('utf-8')).digest():
        return True
    return False

def does_username_exist(username):
    con, cur = connect()
    meloi_found = cur.execute(f'SELECT count(melos_id) FROM melos WHERE username == "{username}"').fetchall()[0][0]
    con.close()
    if meloi_found == 1:
        return True
    return False

def get_melos_id(username):
    con, cur = connect()
    melos_id = cur.execute(f'SELECT melos_id FROM melos WHERE username == "{username}"').fetchall()[0][0]
    con.close()
    return melos_id

def is_mod(username):
    if username is None:
        return False
    con, cur = connect()
    is_mod_int = cur.execute(f'SELECT is_mod FROM melos WHERE username == "{username}"').fetchall()[0][0]
    con.close()
    if is_mod_int == 1:
        return True
    return False

def is_pwlhths(username):
    con, cur = connect()
    is_pwlhths_int = cur.execute(f'SELECT is_pwlhths FROM melos WHERE username == "{username}"').fetchall()[0][0]
    con.close()
    if is_pwlhths_int == 1:
        return True
    return False

def become_pwlhths(username, telephone, afm_mesitikou):
    con, cur = connect()
    melos_id = get_melos_id(username)
    cur.execute(f'INSERT INTO m_pwlhths VALUES ({melos_id}, {telephone}, {afm_mesitikou})')
    cur.execute(f'UPDATE melos SET is_pwlhths = 1 WHERE username == "{username}"')
    con.commit()
    con.close()
