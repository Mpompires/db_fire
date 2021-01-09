from .connect import connect
from .melos import get_melos_id
from .tools import promt

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
        inp_epx['parking_spot'] = int(inp_epx['parking_spot']) if inp_exp['parking_spot'] else None
        inp_epx['construction_year'] = int(inp_epx['construction_year']) if inp_exp['construction_year'] else None
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
