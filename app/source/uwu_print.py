def _max_length_of_table_column(table, index):
    var_max = 0
    for row in table:
        var_max = max(len(str(row[index])), var_max)
    return var_max


def uwu_print(table, column_names):
    if len(table) == 0:
        return None
    assert(len(table[0]) == len(column_names)), "Something wrong with column names"

    row_count = len(table)
    column_count = len(column_names)
    column_max_length = []

    for i in range(column_count):
        max_len_column = max(_max_length_of_table_column(table, i), len(column_names[i]))
        column_max_length.append(max_len_column)

    out = '{:<{max_length}}'.format(column_names[0], max_length=column_max_length[0])
    for i in range(1, column_count):
        out = out + '|' + '{:<{max_length}}'.format(column_names[i], max_length=column_max_length[i])
    print(out)

    for i in range(row_count):
        out = '{:<{max_length}}'.format(str(table[i][0]), max_length=column_max_length[0])
        for j in range(1, column_count):
            out = out + ',' + '{:<{max_length}}'.format(str(table[i][j]), max_length=column_max_length[j])
        print(out)

