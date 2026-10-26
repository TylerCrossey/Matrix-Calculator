from fractions import Fraction
import pytest
import matrix_operations as mo
from shell import MatrixShell

@pytest.fixture
def shell():
    return MatrixShell() #fresh shell made for each test

def shell_with_A(shell, m2x2):
    shell.matrices["A"] = m2x2
    return shell_A

@pytest.fixture
def m2x2():
    return [[Fraction(1), Fraction(1, 2)], 
            [Fraction(3), Fraction(4)]]

@pytest.fixture
def identity2x2():
        return [[Fraction(1), Fraction(0)], 
               [Fraction(0), Fraction(1)]]

#shell functions

def test_set_stores_matrix(shell, m2x2):
    shell.onecmd("set A 1,1/2;3,4")
    assert shell.matrices["A"] == m2x2

#mo helpers TODO: finish reformatting with m2x2

def test_add_multiple(m2x2):
    mo._add_multiple(m2x2, 0, 1, Fraction(2))
    assert m2x2 == [[Fraction(7), Fraction(17, 2)], [Fraction(3), Fraction(4)]]

def test_add_multiple_zero_factor_changes_nothing(m2x2):
    mo._add_multiple(m2x2, 1, 0, Fraction(0))
    assert m2x2 == [[Fraction(1), Fraction(1, 2)], [Fraction(3), Fraction(4)]]

def test_add_multiple_fractional_factor(m2x2):
    mo._add_multiple(m2x2, 1, 0, Fraction(1, 2))
    assert m2x2 == [[Fraction(1), Fraction(1, 2)], [Fraction(7, 2), Fraction(17, 4)]]

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

def test_dot_product():
    a = [Fraction(1), Fraction(2), Fraction(3)]
    b = [Fraction(4), Fraction(-5), Fraction(6)]
    assert mo._dot_product(a, b) == 12

#mo functions

#def test_matrix_mul():

def test_matrix_mul(m2x2):
    assert mo.matrix_mul(m2x2, m2x2) == [
                                [Fraction(5/2), Fraction(5/2)],
                                [Fraction(15), Fraction(35/2)],
                                    ]


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


def test_inverse_of_identity_is_identity(identity2x2):
    assert mo.inverse(identity2x2) == identity2x2


def test_singular_matrix_raises():
    singular = [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(4)]]
    with pytest.raises(ValueError):
        mo.inverse(singular)
