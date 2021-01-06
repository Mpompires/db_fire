from hashlib import sha256
import sqlite3
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

def is_mod(username):
    con, cur = connect()
    is_mod_int = cur.execute(f'SELECT is_mod FROM melos WHERE username == "{username}"').fetchall()[0][0]
    con.close()
    if is_mod_int == 1:
        return True
    return False

def become_pwlhths(username, afm, telephone, is_mesiths):
    con, cur = connect()
    melos_id = cur.execute(f'SELECT melos_id FROM melos WHERE username == "{username}"').fetchall()[0][0]
    if is_mesiths:
        pass
    else:
        cur.execute(f'INSERT INTO m_pwlhths VALUES ({melos_id}, {afm}, {telephone}, 0)')
        cur.execute(f'UPDATE melos SET is_pwlhths = 1 WHERE username == "{username}"')
    con.commit()
    con.close()
