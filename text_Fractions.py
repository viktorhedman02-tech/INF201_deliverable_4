from Fractions import Fraction

def test_add() -> None:
    assert Fraction(1, 2) + Fraction(2, 3) == Fraction(5, 6)

def test_mul() -> None:
    assert Fraction(1, 2) * Fraction(2, 3) == Fraction(2, 6)

def test_div() -> None:
    assert Fraction(1, 2) / Fraction(2, 3) == Fraction(3, 4)

def test_str() -> None:
    assert Fraction(1, 2).__str__ == '1/2'

def test_bol() -> None:
    pass