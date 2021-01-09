from .connect import connect
from .melos import get_melos_id

def does_aggelia_exist(aggelia_id):
    con, cur = connect()
    aggelies_found = cur.execute(f'SELECT count(aggelia_id)'
                                 f'  FROM aggelia '
                                 f'  WHERE aggelia_id == "{aggelia_id}"').fetchall()[0][0]
    con.close()
    if aggelies_found == 1:
        return True
    return False

def does_user_has_edit_privilege_aggelia(username, aggelia_id):
    pwlhths_id = get_melos_id(username)
    con, cur = connect()
    aggelies_found = cur.execute(f'SELECT count(aggelia_id) '
                                 f'   FROM aggelia '
                                 f'   WHERE aggelia_id == "{aggelia_id}" AND pwlhths_id = "{pwlhths_id}"').fetchall()[0][0]
    con.close()
    if aggelies_found == 1:
        return True
    return False

def search_aggelies_katoikia(kat_type,min_price,max_price,heating_system,min_bathrooms,max_bathrooms,min_construction_year,max_construction_year):
    sql = 'SELECT akinhto_id FROM a_katoikia WHERE akinhto_id IS NOT NULL'
    if kat_type == '1':
        sql += ' AND katoikia_type == "monokatoikia"'
    elif kat_type == '2':
        sql += ' AND katoikia_type == "polykatoikia"'
    if heating_system == '1':
        sql += ' AND heating_system == "autonomh"'
    elif heating_system == '2':
        sql += ' AND heating_system == "kentrikh"'
    if min_bathrooms.isdigit():
        min_bathrooms = int(min_bathrooms)
        sql += f' AND bathrooms >= {min_bathrooms}'
    if max_bathrooms.isdigit():
        max_bathrooms = int(max_bathrooms)
        sql += f' AND bathrooms <= {max_bathrooms}'
    if min_construction_year.isdigit():
        min_construction_year = int(min_construction_year)
        sql += f' AND construction_year >= {min_construction_year}'
    if max_construction_year.isdigit():
        max_construction_year = int(max_construction_year)
        sql += f' AND construction_year <= {max_construction_year}'

    con, cur = connect()
    ret = cur.execute(sql).fetchall()
    ret = [row[0] for row in ret]
    sql = 'SELECT a_katoikia.akinhto_id, aggelia.aggelia_type, aggelia.price, aggelia.text, a_katoikia.katoikia_type, a_katoikia.heating_system, a_katoikia.bathrooms, a_katoikia.floor, a_katoikia.construction_year FROM a_katoikia LEFT JOIN aggelia ON aggelia.akinhto_id == a_katoikia.akinhto_id WHERE aggelia_id IS NOT NULL AND a_katoikia.akinhto_id IN ({seq})'.format(seq=','.join(['?'] * len(ret)))
    if min_price.isdigit():
        min_price = int(min_price)
        sql += f' AND aggelia.price >= {min_price}'
    if max_price.isdigit():
        max_price = int(max_price)
        sql += f' AND aggelia.price <= {max_price}'
    ret = cur.execute(sql, ret).fetchall()
    con.close()
    return ret
