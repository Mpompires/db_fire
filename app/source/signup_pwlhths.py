from .connect import connect
from .melos import become_pwlhths

freelancer_virtual_mesitiko_afm = 0

def _if_mesitiko_does_not_exist_add_it(afm):
    con, cur = connect()
    mesitika_found = cur.execute(f'SELECT count(afm) FROM mesitiko_grafeio WHERE afm == "{afm}"').fetchall()[0][0]
    if mesitika_found == 0:
        print('Not such mesitiko exist in database, please add its info')
        brand_name = input('Brand name: ')
        address = input('Address: ')
        cur.execute(f'INSERT INTO mesitiko_grafeio VALUES ("{afm}", "{brand_name}", "{address}")')
        con.commit()
    con.close()

def _add_freelancer_virtual_mesitiko_if_not_exist():
    con, cur = connect()
    mesitika_found = cur.execute(f'SELECT count(afm) FROM mesitiko_grafeio WHERE afm == 0').fetchall()[0][0]
    if mesitika_found == 0:
        cur.execute(f'INSERT INTO mesitiko_grafeio VALUES ({freelancer_virtual_mesitiko_afm}, "(user is freelancer)", "(no info)")')
        con.commit()
    con.close()

def signup_pwlhths(username):
    telephone = input('Telephone: ')
    is_at_mesitiko = input('Se mesitiko grafeio [Y/n]: ')
    if is_at_mesitiko == 'Y' or is_at_mesitiko == 'y':
        mesitiko_afm = input('AFM mesitikou grafeiou: ')
        _if_mesitiko_does_not_exist_add_it(mesitiko_afm)
    else:
        _add_freelancer_virtual_mesitiko_if_not_exist()
        mesitiko_afm = freelancer_virtual_mesitiko_afm
    become_pwlhths(username, telephone, mesitiko_afm)
