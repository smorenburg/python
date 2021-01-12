def create_matrix(rows, cols):
    mtx = []

    for row in range(rows):
        row = []
        for col in range(cols):
            col = 0
            row.append(col)
        mtx.append(row)

    return mtx


def add_matrices(mtx1, mtx2):
    if mtx1 == [] or mtx2 == []:
        return []

    if len(mtx1) != len(mtx2) or len(mtx1[0]) != len(mtx2[0]):
        return []

    rows = len(mtx1)
    cols = len(mtx1[0])
    mtx = create_matrix(rows, cols)

    for row in range(rows):
        for col in range(cols):
            mtx[row][col] = mtx1[row][col] + mtx2[row][col]

    return mtx


def print_matrix(mtx):
    for row in mtx:
        line = ''
        for num in row:
            line += str(num) + ' '
        print(line)


def is_valid_matrix(mtx):
    """
    >>> is_valid_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    True
    >>> is_valid_matrix([[1, 2, 3], [4, 5], [7, 8, 9]])
    False
    """
    if mtx == []:
        return False

    cols = len(mtx[0])

    for col in mtx:
        if len(col) != cols:
            return False

    return True


def multiply_matrices(mtx1, mtx2):
    """
    >>> mtx1 = [[1, 2, 3], [4, 5, 6]]
    >>> mtx2 = [[1, 2], [3, 4], [5, 6]]
    >>> multiply_matrices(mtx1, mtx2)
    [[22, 28], [49, 64]]
    >>> multiply_matrices(mtx2, [])
    >>> multiply_matrices(mtx2, mtx2)
    """
    if not is_valid_matrix(mtx1) or not is_valid_matrix(mtx2):
        return None

    if len(mtx1[0]) != len(mtx2):
        return None

    mtx = create_matrix(len(mtx1), len(mtx2[0]))
    row = 0
    col = 0

    while row < len(mtx1):
        while col < len(mtx2[0]):
            for itr in range(len(mtx1[0])):
                mtx[row][col] += mtx1[row][itr] * mtx2[itr][col]
            col += 1
        row += 1
        col = 0

    return mtx
