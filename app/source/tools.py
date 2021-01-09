from .connect import connect

def get_fields(table_name, exclude_fields):
    con, cur = connect()
    cur.execute(f"SELECT * FROM {table_name}")
    return [member[0] for member in cur.description if member[0] not in exclude_fields]

def promt(table_name, exclude_fields):
    inp = {}
    fields = get_fields(table_name, exclude_fields)
    for field in fields:
        inp[field] = input(f'{field}: ')
    return inp
