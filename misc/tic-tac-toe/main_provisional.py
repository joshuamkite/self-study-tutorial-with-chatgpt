board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

columns = {
    "a": 0,
    "b": 1,
    "c": 2,
}


def get_row_col(ref):
    coords = list(ref)
    row = (int(coords[1])-1)
    column = columns[coords[0]]
    return row, column


if __name__ == '__main__':
    w = input().strip()
    print(get_row_col(w))
