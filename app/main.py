from source import connect
import hashlib

current_user = None

def signup():
    con, cur = connect.connect()
    username = input('Username: ')
    password = hashlib.sha256(input('Password: ').encode('utf-8')).digest()
    email = input('Email: ')
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    is_endiaferomenos = 1
    is_pwlhths = 0
    row = (None, username, password, email, first_name, last_name, is_endiaferomenos, is_pwlhths)
    cur.execute(f"INSERT INTO melos VALUES (?,?,?,?,?,?,?,?)", row)
    con.commit()
    con.close()


while True:
    while current_user == None:
        option = input('Enter l (login) or s (sign up): ')
        if option == 'l': login()
        else: signup()
