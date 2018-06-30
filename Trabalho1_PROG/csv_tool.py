def split_cells(csv,separador):
    temp = ''
    listCells = []
    for i in range(len(csv)):
        if csv[i] != separador:
            temp += csv[i]
        elif len(temp) > 0:
            if temp[0] == '"' and temp[-1] != '"':
                temp += csv[i]
            else:
                listCells.append(temp.strip())
                temp = ''
    if len(temp) > 0:
        listCells.append(temp.strip())

    return listCells


def list_to_table(table_list):
    newTableList = open('new_table.csv', 'wt')
    for cell in table_list:
        line = ';'.join(cell)+'\n'
        newTableList.write(line)

    newTableList.close()


def table_to_list(csv):
    table_list = list()
    table_file = open(csv, "rt")
    columns_meta = table_file.readline()
    table_line = table_file.readline()

    while table_line != "":
        cells = split_cells(table_line,';')
        table_list.append(cells)

        table_line = table_file.readline()

    table_file.close()

    return columns_meta,table_list


def move_columns_to(csv, columns, after='end'):

    for cell in csv:
        cellLen = len(cell)
        increment = 0
        decrement = 0

        for column in columns:
            temp = cell[column-decrement]

            if after == 'end':
                cell.insert(cellLen,temp)
                cell.pop(column-decrement)
            elif after != 'end':
                cell.insert(after+increment, temp)
                cell.pop(column-decrement)

            increment+=1
            decrement+=1
