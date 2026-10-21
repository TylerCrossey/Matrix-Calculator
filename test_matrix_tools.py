from fractions import Fraction
import pytest
import matrix_operations as mo
from shell import MatrixShell

@pytest.fixture
def shell():
    return MatrixShell() #fresh shell made for each test

#shell functions

def test_set_stores_matrix(shell):
    shell.onecmd("set A 1,1/2;3,4")
    assert shell.matrices["A"] == [[Fraction(1), Fraction(1/2)], [Fraction(3), Fraction(4)]]

#mo helpers

def test_add_multiple():
    m = [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]]
    mo._add_multiple(m, 0, 1, Fraction(2))
    assert m == [[Fraction(7), Fraction(10)], [Fraction(3), Fraction(4)]]

def test_add_multiple_zero_factor_changes_nothing():
    m = [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]]
    mo._add_multiple(m, 1, 0, Fraction(0))
    assert m == [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]]

def test_add_multiple_fractional_factor():
    m = [[Fraction(2), Fraction(4)], [Fraction(1), Fraction(1)]]
    mo._add_multiple(m, 1, 0, Fraction(1, 2))
    assert m == [[Fraction(2), Fraction(4)], [Fraction(2), Fraction(3)]]

def test_scale_row():
    m = [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]]
    mo._scale_row(m, 1, Fraction(1, 2))
    assert m == [[Fraction(1), Fraction(2)], [Fraction(3, 2), Fraction(2)]]

def test_find_pivot_row():
    m = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    assert mo._find_pivot_row(m, 0, 0) == 0
    
def test_find_pivot_row_none_in_co():
    m = [[Fraction(0), Fraction(1)], [Fraction(0), Fraction(1)]]
    assert mo._find_pivot_row(m, 0, 0) == None

#mo functions

def test_row_reduce_rank_deficient():
    m = [
        [Fraction(1), Fraction(2)],
        [Fraction(2), Fraction(4)],
    ]
    assert mo.row_reduce(m) == [
        [Fraction(1), Fraction(2)],
        [Fraction(0), Fraction(0)],
    ]

def test_augment():
    left = [
        [Fraction(1), Fraction(2)],
        [Fraction(2), Fraction(4)],
    ]
    identity = [
        [Fraction(1), Fraction(0)], 
        [Fraction(0), Fraction(1)], 
        ]
    assert mo._augment(left, identity) == [
        [Fraction(1), Fraction(2), Fraction(1), Fraction(0)],
        [Fraction(2), Fraction(4), Fraction(0), Fraction(1)],
        ]


def test_inverse_of_identity_is_identity():
    mo.identity = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    assert inverse(identity) == identity


def test_singular_matrix_raises():
    singular = [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(4)]]
    with pytest.raises(ValueError):
        mo.inverse(singular)
