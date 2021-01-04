from .melos import become_pwlhths

def signup_pwlhths(username):
    telephone = input('Telephone: ')
    afm = input('Afm: ')
    is_mesiths = input('1 (Mesiths) or 2 (Regular)')
    if is_mesiths == '2':
        become_pwlhths(username, telephone, afm, 0)
    return username
