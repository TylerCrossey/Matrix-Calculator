from fractions import Fraction

import pytest

from matrix_operations import inverse


def test_inverse_of_identity_is_identity():
    identity = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    assert inverse(identity) == identity


def test_singular_matrix_raises():
    singular = [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(4)]]
    with pytest.raises(ValueError):
        inverse(singular)