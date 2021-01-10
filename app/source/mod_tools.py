from .connect import connect
from .melos import does_username_exist
from .printer import print_table,print_row

def mod_sign_as(*args):
    as_username = input("Sign as: ")
    if not does_username_exist(as_username):
        print("This user does not exist")
    else:
        return as_username

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
                               f'   JOIN aggelia ag ON ag.pwlhths_id = p.melos_id'
                               f'   JOIN akinhto ak ON ak.diaxhrizetai_pwlhths_id = p.melos_id'
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
                               f'   JOIN aggelia ag ON ag.pwlhths_id = p.melos_id'
                               f'   JOIN akinhto ak ON ak.diaxhrizetai_pwlhths_id = p.melos_id'
                               f'   GROUP BY p.melos_id'
                               f'   ORDER BY count(DISTINCT ag.aggelia_id) DESC').fetchall()
    con.close()
    print_table(result_table,
                ['Username', ['Επώνυμο', 25], ['Όνομα', 25], 'Πλήθος αγγελιών', 'Πλήθος διαχ. ακινήτων', ['Μεσιτικό γραφείο', 25]])
