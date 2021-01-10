from hashlib import sha256
from .connect import connect
from .melos import does_username_exist, is_mod, insert_melos
from .printer import print_table

def add_root_if_not_exist():
    root_username = "root"
    root_password = "root"

    if does_username_exist(root_username) and is_mod(root_username):
        return None
    else:
        print("No root found, adding...")
        username = root_username
        password = sha256(root_password.encode('utf-8')).digest()
        email = "-"
        first_name = "root"
        last_name = "root"
        user_is_endiaferomenos = 0
        user_is_pwlhths = 0
        user_is_mod = 1
        row = (None, username, password, email, first_name, last_name, user_is_endiaferomenos, user_is_pwlhths, user_is_mod)
        insert_melos(row)

def mod_sign_as(*args):
    as_username = input("Sign as: ")
    if not does_username_exist(as_username):
        print("This user does not exist")
    else:
        return as_username

def mod_appoint_new_mod(*args):
    username_of_new_mod = input("Username of new mod: ")
    if not does_username_exist(username_of_new_mod):
        print("No such user..")
    elif is_mod(username_of_new_mod):
        print("User is already a mod")
    else:
        con, cur = connect()
        cur.execute(f'UPDATE melos SET is_mod = 1 WHERE username == "{username_of_new_mod}"')
        con.commit()
        con.close()

def mod_list_akinhta_idiokthth(*args):
    first_name = input("First name of idiokthth: ")
    last_name = input("Last name of idiokthth: ")

    queue = (f'SELECT akinhto_id, surface_area, area, area_coords, description, extra, akinhto_type, username'
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
                ['ID ακινήτου', 'Εμβαδόν', 'Περιοχή', 'Συντεταγμένες', ['Περιγραφή', 25], ['Επιπρόσθετες πληροφορίες', 25], 'Τύπος ακινήτου', 'Username Πωλητή'])

def mod_list_mesitika_grafeia(*args):
    con, cur = connect()
    result_table = cur.execute(f'SELECT mg.afm, mg.brand_name, mg.brand_address, count(DISTINCT p.melos_id), count(DISTINCT ag.aggelia_id), count(DISTINCT ak.akinhto_id)'
                               f'  FROM m_pwlhths p '
                               f'   JOIN mesitiko_grafeio mg ON p.mesitiko_grafeio_afm = mg.afm'
                               f'   LEFT JOIN aggelia ag ON ag.pwlhths_id = p.melos_id'
                               f'   LEFT JOIN akinhto ak ON ak.diaxhrizetai_pwlhths_id = p.melos_id'
                               f'   GROUP BY mg.afm'
                               f'   ORDER BY count(DISTINCT ag.aggelia_id) DESC').fetchall()
    con.close()
    print_table(result_table,
                ['ΑΦΜ', ['Όνομα', 25], ['Διεύθυνση', 25], 'Εγγεγραμένοι Πωλητές', 'Συνολικές αγγελίες', 'Συνολικά διαχ. ακίνητα'])

def mod_list_pwlhtes(*args):
    con, cur = connect()
    result_table = cur.execute(f'SELECT username, first_name, last_name, count(DISTINCT ag.aggelia_id), count(DISTINCT ak.akinhto_id), brand_name'
                               f'  FROM m_pwlhths p '
                               f'   JOIN melos m ON p.melos_id = m.melos_id '
                               f'   JOIN mesitiko_grafeio mg ON p.mesitiko_grafeio_afm = mg.afm'
                               f'   LEFT JOIN aggelia ag ON ag.pwlhths_id = p.melos_id'
                               f'   LEFT JOIN akinhto ak ON ak.diaxhrizetai_pwlhths_id = p.melos_id'
                               f'   GROUP BY p.melos_id'
                               f'   ORDER BY count(DISTINCT ag.aggelia_id) DESC').fetchall()
    con.close()
    print_table(result_table,
                ['Username', ['Επώνυμο', 25], ['Όνομα', 25], 'Πλήθος αγγελιών', 'Πλήθος διαχ. ακινήτων', ['Μεσιτικό γραφείο', 25]])
