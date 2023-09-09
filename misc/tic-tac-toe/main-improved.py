columns = {
    "A": 0,
    "B": 1,
    "C": 2,
}


def get_row_col(ref):
    row = (int((list(ref))[1])-1)
    column = columns[(list(ref))[0]]
    return row, column
