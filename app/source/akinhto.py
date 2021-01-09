from .connect import connect
from .tools import promt
from .melos import get_melos_id, is_mod
from .printer import print_row, match_column_with_dictionary

def does_akinhto_exist(akinhto_id):
    con, cur = connect()
    aggelies_found = cur.execute(f'SELECT count(akinhto_id)'
                                 f'  FROM akinhto '
                                 f'  WHERE akinhto_id == "{akinhto_id}"').fetchall()[0][0]
    con.close()
    if aggelies_found == 1:
        return True
    return False

def _is_user_akinhto_manager(username, akinhto_id):
    pwlhths_id = get_melos_id(username)
    con, cur = connect()
    aggelies_found = cur.execute(f'SELECT count(akinhto_id) '
                                 f'   FROM akinhto '
                                 f'   WHERE akinhto_id = "{akinhto_id}" AND diaxhrizetai_pwlhths_id = "{pwlhths_id}"').fetchall()[0][0]
    con.close()
    if aggelies_found == 1:
        return True
    return False

def does_user_has_edit_privilege_aggelia(username, akinhto_id):
    if _is_user_akinhto_manager(username, akinhto_id) or is_mod(username):
        return True
    return False

def create_akinhto(current_user):
    con, cur = connect()
    inp = promt('akinhto', ['akinhto_id', 'diaxhrizetai_pwlhths_id'])
    inp['surface_area'] = float(inp['surface_area']) if inp['surface_area'] else None
    inp['akinhto_id'] = None
    inp['diaxhrizetai_pwlhths_id'] = get_melos_id(current_user)
    if inp['akinhto_type'] == 'katoikia':
        cur.execute('INSERT INTO akinhto VALUES(:akinhto_id, :surface_area, :area, :area_coords, :description, :extra,'
            ':diaxhrizetai_pwlhths_id, :first_name_idiokthth, :last_name_idiokthth, :akinhto_type)', inp)
        inp_kat = promt('a_katoikia', ['akinhto_id'])
        inp_kat['akinhto_id'] = cur.lastrowid
        inp_kat['bathrooms'] = int(inp_kat['bathrooms']) if inp_kat['bathrooms'] else None
        inp_kat['floor'] = int(inp_kat['floor']) if inp_kat['floor'] else None
        inp_kat['construction_year'] = int(inp_kat['construction_year']) if inp_kat['construction_year'] else None
        cur.execute('INSERT INTO a_katoikia VALUES(:akinhto_id, :katoikia_type, :heating_system, :bathrooms, :floor,'
            ':construction_year, :internal, :external)', inp_kat)
        con.commit()
        print('Successfully added akinhto katoikia..')
    elif inp['akinhto_type'] == 'epaggelmatikos_xwros':
        cur.execute('INSERT INTO akinhto VALUES(:akinhto_id, :surface_area, :area, :area_coords,'
            ':description, :extra, :diaxhrizetai_pwlhths_id, :first_name_idiokthth, :last_name_idiokthth, :akinhto_type)', inp)
        inp_epx = promt('a_epaggelmatikos_xwros', ['akinhto_id'])
        inp_epx['parking_spot'] = int(inp_epx['parking_spot']) if inp_epx['parking_spot'] else None
        inp_epx['construction_year'] = int(inp_epx['construction_year']) if inp_epx['construction_year'] else None
        inp_epx['akinhto_id'] = cur.lastrowid
        cur.execute('INSERT INTO a_epaggelmatikos_xwros VALUES(:akinhto_id, :parking_spot, :construction_year, :internal, :external)', inp_epx)
        con.commit()
        print('Successfully added akinhto epaggelmatikos_xwros..')
    elif inp['akinhto_type'] == 'gh':
        cur.execute('INSERT INTO akinhto VALUES(:akinhto_id, :surface_area, :area, :area_coords, :description, :extra,'
            ':diaxhrizetai_pwlhths_id, :first_name_idiokthth, :last_name_idiokthth, :akinhto_type)', inp)
        inp_gh = promt('a_gh',['akinhto_id'])
        inp_gh['akinhto_id'] = cur.lastrowid
        inp_gh['building_coeff'] = float(inp_gh['building_coeff']) if inp_gh['building_coeff'] else None
        cur.execute('INSERT INTO a_gh VALUES(:akinhto_id, :building_coeff, :external)', inp_gh)
        con.commit()
        print('Successfully added akinhto gh..')
    else:
        print('Invalid akinhto_type..')
    con.close()
    return current_user

def _print_katoikia(akinhto_id):
    con, cur = connect()
    katoikia_row = cur.execute(f'SELECT katoikia_type, heating_system, bathrooms, floor, construction_year, internal, "external"'
                               f'   FROM a_katoikia'
                               f'   WHERE akinhto_id = {akinhto_id}').fetchall()
    con.close()

    katoikia_row = match_column_with_dictionary(katoikia_row, {'polykatoikia':'Πολυκατοικία', 'monokatoikia':'Μονοκατοικία'}, 0)
    katoikia_row = match_column_with_dictionary(katoikia_row, {'autonomh':'Αυτόνομη', 'kentrikh':'Κεντρική'}, 1)
    print_row(katoikia_row[0],
              ['Τύπος κατοικίας', 'Σύστημα θέρμανσης', 'Μπάνια', 'Όροφος', 'Έτος κατασκευής', 'Εσωτερικά', 'Εξωτερικά'])

def _print_epaggelmatikos_xwros(akinhto_id):
    con, cur = connect()
    epgxwr_row = cur.execute(f'SELECT parking_spot, construnction_year, internal, "external"'
                             f'   FROM a_epaggelmatikos_xwros'
                             f'   WHERE akinhto_id = {akinhto_id}').fetchall()
    con.close()

    epgxwr_row = match_column_with_dictionary(epgxwr_row, {0:'Όχι', 1:'Ναί'}, 0)
    print_row(epgxwr_row[0],
              ['Χώρος Στάθμεσης', 'Έτος κατασκευής', 'Εσωτερικά', 'Εξωτερικά'])

def _print_gh(akinhto_id):
    con, cur = connect()
    gh_row =cur.execute(f'SELECT building_coeff, "external"'
                        f'   FROM a_gh'
                        f'   WHERE akinhto_id = {akinhto_id}').fetchall()
    con.close()

    print_row(gh_row[0],
              ['Συντελεστής Δόμησης', 'Εξωτερικά'])

def _print_akinhto_type(akinhto_id, akinhto_type):
    if akinhto_type == 'katoikia':
        _print_katoikia(akinhto_id)
    elif akinhto_type == 'epaggelmatikos_xwros':
        _print_epaggelmatikos_xwros(akinhto_id)
    elif akinhto_type == 'gh':
        _print_gh(akinhto_id)

def print_akinhto(akinhto_id):
    con, cur = connect()
    akinhto_row =cur.execute(f'SELECT surface_area, area, area_coords, akinhto_type, description, extra'
                             f'   FROM akinhto'
                             f'   WHERE akinhto_id = {akinhto_id}').fetchall()
    con.close()
    akinhto_type = akinhto_row[0][3]

    akinhto_row_matched = match_column_with_dictionary(akinhto_row, {'epaggelmatikos_xwros':'Επαγγελματικός Χώρος', 'katoikia':'Κατοικία', 'gh': 'Γη'}, 3)
    print_row(akinhto_row_matched[0],
              ['Τετραγωνικά', 'Περιοχή', 'Συντεταγμένες', 'Τύπος ακινήτου', 'Περιγραφή', 'Επιπλέον Πληροφορίες'])
    _print_akinhto_type(akinhto_id, akinhto_type)

def print_akinhto_full(akinhto_id):
    con, cur = connect()
    akinhto_row =cur.execute(f'SELECT surface_area, area, area_coords, akinhto_type, description, extra, username, first_name_idiokthth, last_name_idiokthth'
                             f'   FROM akinhto JOIN melos ON diaxhrizetai_pwlhths_id = melos_id' 
                             f'   WHERE akinhto_id = {akinhto_id}').fetchall()
    con.close()
    akinhto_type = akinhto_row[0][3]

    akinhto_row_matched = match_column_with_dictionary(akinhto_row, {'epaggelmatikos_xwros':'Επαγγελματικός Χώρος', 'katoikia':'Κατοικία', 'gh': 'Γη'}, 3)
    print_row(akinhto_row_matched[0],
              ['Τετραγωνικά', 'Περιοχή', 'Συντεταγμένες', 'Τύπος ακινήτου', 'Περιγραφή', 'Επιπλέον Πληροφορίες', 'Username Πωλητή', 'Όνομα Ιδιοκτήτη', 'Επώνυμο Ιδιοκτήτη'])
    _print_akinhto_type(akinhto_id, akinhto_type)
