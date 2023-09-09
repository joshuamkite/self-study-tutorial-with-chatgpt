columns = {
    "A": 0,
    "B": 1,
    "C": 2,
}


def get_row_col(ref):
    coords = list(ref)
    row = (int(coords[1])-1)
    column = columns[coords[0]]
    return row, column
