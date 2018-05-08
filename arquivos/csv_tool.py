def separaPal(texto):
    listaPal = []
    temp = ""
    for i in range(len(texto)):

        if texto[i].isalnum() or texto[i] == '"':
            temp += texto[i]
        elif len(temp) > 0: # nome, "teste, teste", id
            if temp[0] == "\"" and temp[-1] != '"' :
                temp += texto[i]
            else:
                listaPal.append(temp)
                temp = ""

    if len(temp) > 0:
        listaPal.append(temp)

    return listaPal

def split_cells(csv):
    for i in range(len(texto)):
        

def table_to_dict(csv):
    table_dict = dict()
    table_file = open(csv, "rt")
    table_file.readline()
    table_line = table_file.readline()
    while table_line != "":
        print(table_line)
        print(separaPal(table_line))
        table_line = table_file.readline()

    table_file.close()

def move_columns_to_end(csv, columns):
    return 0


def main(args):
    table_dict = table_to_dict(args[1])
    newTable = move_columns_to_end(args[1], (0,1))


if __name__ == "__main__":
    import sys
    main(sys.argv)