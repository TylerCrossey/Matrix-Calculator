""" Matrix operations: row reduction and inversion """

from fractions import Fraction

Matrix = list[list[Fraction]]

def _swap_rows(m: Matrix, i: int, j: int) -> None:
    """Swap rows i and j of m in place."""
    raise NotImplementedError

def _scale_row(m: Matrix, i: int, factor: Fraction) -> None:
    """Multiply row i by factor in place."""
    raise NotImplementedError

def _add_multiple(m: Matrix, target: int, source: int, factor: Fraction) -> None:
    """Row[target] += factor * Row[source]."""
    raise NotImplementedError


def row_reduce(matrix: Matrix) -> Matrix:
    """Return the reduced echelon form of a matrix.

    Copy the input matrix to be edited


    
    The input is not modified.
    """

    raise NotImplementedError

def _identity(n: int) -> Matrix:
    """Return the identity matrix of size nxn."""
    raise NotImplementedError

def _augment(left: Matrix, right: Matrix) -> Matrix:
    """Return left matrix augmented with right matrix"""
    raise NotImplementedError

def inverse(matrix: Matrix) -> Matrix:
    """Return the inverse of a square matrix.

    Raises
        ValueError: if the matrix is not square or is singular.
    """

    raise NotImplementedError
