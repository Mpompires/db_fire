from .connect import connect
from .melos import get_melos_id
from .printer import print_table

def list_my_aggelies(username):
    pwlhths_id = get_melos_id(username)

    con, cur = connect()
    aggelies_found = cur.execute(f'SELECT ag.aggelia_id, ak.akinhto_id, ak.akinhto_type, ag.aggelia_type, ag.price, ak.area, ak.surface_area, ag.available, ag.text'
                                 f'   FROM aggelia ag JOIN akinhto ak ON ag.akinhto_id = ak.akinhto_id'
                                 f'   WHERE pwlhths_id == "{pwlhths_id}"'
                                 f'   ORDER BY ag.available DESC, ak.akinhto_type, ag.aggelia_type, ag.price').fetchall()
    con.close()

    print_table(aggelies_found,
                ['ID Αγγελίας', 'ID Ακινήτου', 'Τύπος ακινήτου', 'Πωλ./Εν.', 'Τιμή', 'Περιοχή', 'Τετραγωνικά', 'Διαθέσιμο', ['Σημειώσεις', 25]])

def list_my_akinhta(username):
    pwlhths_id = get_melos_id(username)

    con, cur = connect()
    akinhta_found = cur.execute(f'SELECT akinhto_id, akinhto_type, area, surface_area, description'
                                 f'   FROM akinhto'
                                 f'   WHERE diaxhrizetai_pwlhths_id == "{pwlhths_id}"').fetchall()
    con.close()
    print_table(akinhta_found,
                ['ID Ακινήτου', 'Τύπος ακινήτου', 'Περιοχή', 'Τετραγωνικά', ['Περιγραφή', 30]])