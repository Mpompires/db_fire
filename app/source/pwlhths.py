from .connect import connect
from .melos import get_melos_id, is_freelancer
from .printer import print_table, print_row, match_column_with_dictionary

def list_my_aggelies(username):
    pwlhths_id = get_melos_id(username)

    con, cur = connect()
    aggelies_found = cur.execute(f'SELECT ag.aggelia_id, ak.akinhto_id, ak.akinhto_type, ag.aggelia_type, ag.price, ak.area, ak.surface_area, ag.available, ag.text'
                                 f'   FROM aggelia ag JOIN akinhto ak ON ag.akinhto_id = ak.akinhto_id'
                                 f'   WHERE pwlhths_id == "{pwlhths_id}"'
                                 f'   ORDER BY ag.available DESC, ak.akinhto_type, ag.aggelia_type, ag.price').fetchall()
    con.close()

    aggelies_found = match_column_with_dictionary(aggelies_found, {0:'Όχι', 1:'Ναί'}, 7)
    aggelies_found = match_column_with_dictionary(aggelies_found, {'enoikiazetai':'Ενοικιάζεται', 'pwleitai':'Πωλείται'}, 3)
    aggelies_found = match_column_with_dictionary(aggelies_found, {'epaggelmatikos_xwros':'Επαγγελματικός Χώρος', 'katoikia':'Κατοικία', 'gh': 'Γη'}, 2)
    print_table(aggelies_found,
                ['ID Αγγελίας', 'ID Ακινήτου', 'Τύπος ακινήτου', 'Πωλ./Εν.', 'Τιμή', 'Περιοχή', 'Τετραγωνικά', 'Διαθέσιμο', ['Σημειώσεις', 25]])

def list_my_akinhta(username):
    pwlhths_id = get_melos_id(username)

    con, cur = connect()
    akinhta_found = cur.execute(f'SELECT akinhto_id, akinhto_type, area, surface_area, description'
                                f'   FROM akinhto'
                                f'   WHERE diaxhrizetai_pwlhths_id == "{pwlhths_id}"'
                                f'   ORDER BY akinhto_type, surface_area').fetchall()
    con.close()

    akinhta_found = match_column_with_dictionary(akinhta_found, {'epaggelmatikos_xwros':'Επαγγελματικός Χώρος', 'katoikia':'Κατοικία', 'gh': 'Γη'}, 1)
    print_table(akinhta_found,
                ['ID Ακινήτου', 'Τύπος ακινήτου', 'Περιοχή', 'Τετραγωνικά', ['Περιγραφή', 30]])

def print_contact_info(username):
    con, cur = connect()
    if is_freelancer(username):
        info_row = cur.execute(f'SELECT m.melos_id, first_name, last_name, telephone, email'
                               f'   FROM melos m JOIN m_pwlhths p ON m.melos_id = p.melos_id'
                               f'   WHERE m.username = "{username}"').fetchall()
        print_row(info_row[0],
                  ['ID', 'Όνομα', 'Επώνυμο', 'Τηλέφωνο', 'e-mail'])
    else:

        info_row = cur.execute(f'SELECT m.melos_id, first_name, last_name, telephone, email, brand_name, brand_address'
                               f'   FROM melos m JOIN m_pwlhths p ON m.melos_id = p.melos_id JOIN mesitiko_grafeio m_g ON p.mesitiko_grafeio_afm = m_g.afm'
                               f'   WHERE m.username = "{username}"').fetchall()
        print_row(info_row[0],
                  ['ID', 'Όνομα', 'Επώνυμο', 'Τηλέφωνο', 'e-mail', 'Μεσιτικό γραφείο', 'Διεύθυνση μεσισικού γραφείου'])
    con.close()