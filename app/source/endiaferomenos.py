from .melos import become_endiaferomenos,get_melos_id
from .connect import connect

def signup_endiaferomenos(username):
    become_endiaferomenos(username)
    print("You are endiaferomenos now!")

def does_endiaferomenos_endiaferetai(username, aggelia_id):
    if username is None:
        return False

    melos_id = get_melos_id(username)
    con, cur = connect()
    end_found = cur.execute(f'SELECT count(*) '
                            f'  FROM m_endiaferomenos_endiaferetai'
                            f'  WHERE melos_id = "{melos_id}" AND aggelia_id = "{aggelia_id}"').fetchall()[0][0]
    con.close()
    if end_found == 1:
        return True
    return False

def endiaferetai_for_aggelia(username):
    aggelia_id = input("aggelia_id: ")

    if does_endiaferomenos_endiaferetai(username, aggelia_id):
        print("Already endiaferesai")
        return

    melos_id = get_melos_id(username)
    con, cur = connect()
    cur.execute(f'INSERT INTO m_endiaferomenos_endiaferetai VALUES ("{melos_id}", "{aggelia_id}")')
    con.commit()
    con.close()