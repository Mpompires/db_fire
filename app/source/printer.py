
def _trim_string(string, max_size):
    dots_count = 2
    if len(string) > max_size:
        return string[0:max_size-dots_count] + '.'*dots_count
    return string


def _columns_trim(table, columns):
    rows_count = len(table)
    columns_count = len(columns)

    return_columns = []
    for this_column in columns:
        if isinstance(this_column, list):
            return_columns.append(_trim_string(this_column[0], this_column[1]))
        else:
            return_columns.append(this_column)

    return_table = []
    for i in range(rows_count):
        result_this_row = []
        for j in range(columns_count):
            if isinstance(columns[j], list) and isinstance(table[i][j], str):
                result_this_row.append(_trim_string(table[i][j], columns[j][1]))
            else:
                result_this_row.append(table[i][j])
        return_table.append(result_this_row)

    return return_table, return_columns


def _max_length_of_table_column(table, index):
    var_max = 0
    for row in table:
        var_max = max(len(str(row[index])), var_max)
    return var_max


def print_table(table, columns):
    if len(table) == 0:
        return None
    assert(len(table[0]) == len(columns)), "Something wrong with column names"

    table, columns = _columns_trim(table, columns)

    row_count = len(table)
    column_count = len(columns)
    column_max_length = []

    for i in range(column_count):
        max_len_column = max(_max_length_of_table_column(table, i), len(columns[i]))
        column_max_length.append(max_len_column)

    out = '{:<{max_length}}'.format(columns[0], max_length=column_max_length[0])
    for i in range(1, column_count):
        out = out + '|' + '{:<{max_length}}'.format(columns[i], max_length=column_max_length[i])
    print(out)

    for i in range(row_count):
        out = '{:<{max_length}}'.format(str(table[i][0]), max_length=column_max_length[0])
        for j in range(1, column_count):
            out = out + ' ' + '{:<{max_length}}'.format(str(table[i][j]), max_length=column_max_length[j])
        print(out)


def print_row(row, columns):
    max_line_size = 80
    colon = ': '
    for i in range(len(columns)):
        this_column_name_length = len(columns[i] + colon)
        this_column_output = str(row[i])
        this_column_output_length = len(this_column_output)

        out = columns[i] + colon
        for i in range(this_column_output_length // (max_line_size - this_column_name_length) + 1):
            start = i*(max_line_size - this_column_name_length)
            end = min((i + 1)*(max_line_size - this_column_name_length), this_column_output_length)
            if i == 0:
                out = out + this_column_output[start: end]
            else:
                out = out + ' '*this_column_name_length + this_column_output[start: end]
            out += '\n'

        print(out, end='')


def match_column_with_dictionary(table, dict, col_index):
    res_table = [list(row) for row in table]
    for i in range(len(table)):
        search_result = dict.get(table[i][col_index])
        if search_result is not None:
            res_table[i][col_index] = search_result
    return res_table
