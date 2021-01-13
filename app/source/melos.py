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

def is_freelancer(username):
    con, cur = connect()
    freelancer_count = cur.execute(f'SELECT count(*) '
                                   f'  FROM melos m JOIN m_pwlhths p ON m.melos_id = p.melos_id'
                                   f'  WHERE m.username = "{username}" AND p.mesitiko_grafeio_afm = 0').fetchall()[0][0]
    con.close()
    if freelancer_count == 1:
        return True
    return False

def is_endiaferomenos(username):
    con, cur = connect()
    is_endiaferomenos_int = cur.execute(f'SELECT is_endiaferomenos FROM melos WHERE username == "{username}"').fetchall()[0][0]
    con.close()
    if is_endiaferomenos_int == 1:
        return True
    return False

def become_pwlhths(username, telephone, afm_mesitikou):
    con, cur = connect()
    melos_id = get_melos_id(username)
    cur.execute(f'INSERT INTO m_pwlhths VALUES ({melos_id}, {telephone}, {afm_mesitikou})')
    cur.execute(f'UPDATE melos SET is_pwlhths = 1 WHERE username == "{username}"')
    con.commit()
    con.close()

def become_endiaferomenos(username):
    con, cur = connect()
    melos_id = get_melos_id(username)
    cur.execute(f'INSERT INTO m_endiaferomenos VALUES ({melos_id})')
    cur.execute(f'UPDATE melos SET is_endiaferomenos = 1 WHERE username == "{username}"')
    con.commit()
    con.close()

def get_aggelies_endiaferomenos(username):
    con, cur = connect()
    melos_id = get_melos_id(username)
    res = cur.execute(f'SELECT m_endiaferomenos_endiaferetai.aggelia_id FROM m_endiaferomenos_endiaferetai WHERE melos_id == "{melos_id}"')
    print(res.fetchall())
    con.commit()
    con.close()
    return username
