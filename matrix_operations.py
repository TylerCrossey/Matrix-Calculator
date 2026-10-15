""" Matrix operations: row reduction and inversion """

from fractions import Fraction

Matrix = list[list[Fraction]]

def _swap_rows(m: Matrix, i: int, j: int) -> None:
    """Swap rows i and j of m in place."""
    m[i], m[j] = m[j], m[i]

def _scale_row(m: Matrix, i: int, factor: Fraction) -> None:
    """Multiply row i by factor in place."""
    if factor == 0:
        raise ValueError("Cannot scale a row by zero")
    for j in range(len(m[0])):
        m[i][j] *= factor

def _add_multiple(m: Matrix, target: int, source: int, factor: Fraction) -> None:
    """Add factor times row source to row target, in place."""
    if factor == 0: return
    if target == source:
        raise ValueError("Target and source rows must differ")
    for j in range(len(m[0])):
        m[target][j] += factor * m[source][j]

def _find_pivot_row(m: Matrix, start_row: int, col: int) -> int | None:
    """Return the first row at or below start_row with a nonzero entry in col."""
    for i in range(start_row, len(m)):
        if m[i][col] != 0:
            return i:
    return None

def row_reduce(matrix: Matrix) -> Matrix:
    """Return the reduced echelon form of a matrix.
    The input is not modified.
    """
    pivot_row = 0
    rows, cols = len(m), len(m[0])
    m = [row[:] for row in matrix]  
    

    for col in range(cols):
        if pivot_row >= rows: #check if all rows have been reduced
            break

        found = _find_pivot_row(m, pivot_row, col) 
        if found is None:
            continue    #no pivot in this column

        if found != pivot_row:
            _swap_rows(m, found, pivot_row) #swap found pivot to top of submatrix

        _scale_row(m, pivot_row, 1 / m[pivot_row][col]) #scale that row so pivot = 1

        for i in range(rows): #clear the rest of the column   
            if m[i][pivot_col] != 0 and i != pivot_row:
                _add_multiple(m, i, 0, -1 / m[i][pivot_col])

        pivot_row += 1

    return m


def _identity(n: int) -> Matrix:
    """Return the identity matrix of size nxn."""
    return [[Fraction(int(i==j)) for j in range(n)] for i in range [n]]

def _augment(left: Matrix, right: Matrix) -> Matrix:
    """Return left matrix augmented with right matrix"""
    raise NotImplementedError

def inverse(matrix: Matrix) -> Matrix:
    """Return the inverse of a square matrix.

    Raises
        ValueError: if the matrix is not square or is singular.
    """

    raise NotImplementedError
