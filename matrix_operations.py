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
    
    m = [row[:] for row in matrix]  #copy the input matrix
    
    #find leftmost non-zero column
    for j in range(len(m)):
        for i in range(len(m[0])):
            if(m[i][j] != 0):
                pivot_col = j
                if(i != 0): #if top of pivot column = 0, swap it with a row of nonzero value
                    _swap_rows(m, i, 0)
                break
    
    
    #scale that row so pivot = 1
    _scale_row(m, 0, 1 / m[0][pivot_col])

    #use add multiple to zero the rest of the column
    for i in range(len(m)):
        if(m[i][pivot_col] != 0):
            _add_multiple(m, i, 0, -1 / m[0][pivot_col])

    #ignoring pivot row and rows above, repeat


    raise NotImplementedError


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
