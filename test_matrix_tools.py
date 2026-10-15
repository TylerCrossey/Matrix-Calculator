from fractions import Fraction

import pytest

import matrix_operations as mo

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


def test_row_reduce_zero_matrix():
    zero_matrix = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]]
    with pytest.raises(ValueError):
        mo.row_reduce(zero_matrix)


def test_inverse_of_identity_is_identity():
    mo.identity = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    assert inverse(identity) == identity


def test_singular_matrix_raises():
    singular = [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(4)]]
    with pytest.raises(ValueError):
        mo.inverse(singular)
