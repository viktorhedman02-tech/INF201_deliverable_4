from Fractions import Fraction

def test_add() -> None:
    resoult1 = Fraction(1, 2) + Fraction(2, 3)
    resoult2 = Fraction(1, 2) + Fraction(1, 2)
    resoult3 = Fraction(1, 2) + 3

    assert resoult1 == Fraction(7, 6)
    assert resoult2 == Fraction(2, 2)
    assert resoult3 == Fraction(7, 2)

def test_mul() -> None:
    assert Fraction(1, 2) * Fraction(2, 3) == Fraction(2, 6)

def test_div() -> None:
    assert Fraction(1, 2) / Fraction(2, 3) == Fraction(3, 4)

def test_str() -> None:
    assert str(Fraction(1, 2)) == "1/2"
    assert str(Fraction(6, 4)) == "6/4"


def test_bol() -> None:
    pass