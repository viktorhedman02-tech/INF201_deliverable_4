from Fractions import Fraction
import pytest 

def test_init():
    '''A test that uses assert to chek if the init function gives the right values'''
    frac = Fraction(1, 2)
    assert frac.numerator == 1
    assert frac.denominator == 2

    frac = Fraction(-1, 2)
    assert frac.numerator == -1
    assert frac.denominator == 2

'''A pytest.mark.paremetrize tha contain values for the test of the cheks for the init methode'''
@pytest.mark.parametrize('num, den, expected',
                         [(1, -2, ValueError), #A Paramiter for cheking if a negativ denoninator rasses a valu error
                         (1, 0, ZeroDivisionError),#A Paramiter for cheking denominator with valu zero rasses a zero divide error
                         (1.2, 2, ValueError),#A Paramiter for cheking if a nunerator as a float rasses a valuerror 
                         (1, 2.3, ValueError),#A Paramiter for cheking if a denominator as a float rasses a valu error
                         (1.2, 2.3, ValueError)]#A Paramiter for cheking if both the denominator and numerator are folats a valur error is raised
)

def test_init_error(num, den, expected):
    '''A test that uses pytest.raises and the pytest.mark.parametrize() from erlyar to chek
    if the if statments and erorr raises work.
    '''
    with pytest.raises(expected):
        Fraction(num, den)

def test_add() -> None:
    '''A Test that cheks the add function using assertions'''

    #Calculates diffrent sumations betweb diffrent fractions and values
    resoult1 = Fraction(1, 2) + Fraction(2, 3)
    resoult2 = Fraction(1, 2) + Fraction(1, 2)
    resoult3 = Fraction(1, 2) + 3
    resoult4 = Fraction(1, 2) + 1.2

    # Test if the resualts gives egspexted values and resualt
    assert resoult1 == Fraction(7, 6)
    assert resoult2 == Fraction(2, 2)
    assert resoult3 == Fraction(7, 2)
    #Test if the correct error is reased
    assert resoult4 == NotImplementedError

def test_mul() -> None:
    '''A test that checs the mul function usins assertions'''

    #Tests diffrent multiplications between difrent fractions and values
    assert Fraction(1, 2) * Fraction(2, 3) == Fraction(2, 6)
    assert Fraction(1, 2) * 2 == Fraction(2, 2)
    #Test if the correct error is reast for a multiplication between a fraction and a float
    assert Fraction(1, 2) * 2.5 == NotImplementedError

def test_div() -> None:
    '''A test that checs the div function usins assertions'''

    #
    assert Fraction(1, 2) / Fraction(2, 3) == Fraction(3, 4)
    assert Fraction(1, 2) / 3 == Fraction(1, 6)
    #
    assert Fraction(1, 2) / 1.2 == NotImplementedError

def test_str() -> None:
    '''A test that checs the str function usins assertions'''

    #Test if the fractions gives the right strings
    assert str(Fraction(1, 2)) == "1/2"
    assert str(Fraction(6, 4)) == "6/4"


def test_bol() -> None:
    '''A test that checs the boolean functions function usins assertions'''
    #Test if the boolean terms give the right true value fore the diffrent fractions and values
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(1, 2) != Fraction(2, 3)
    assert Fraction(1, 3) != 1
    assert Fraction(1, 3) <= Fraction(2, 3)
    assert Fraction(1, 3) >= Fraction(2, 6)
    assert Fraction(5 ,6) > Fraction(2, 3)
    assert Fraction(2 ,6) < Fraction(2, 3)
    assert Fraction(4, 8) < 2
    assert Fraction(4, 8) <= 2
    #Test if the boolena espretions gives the right false values. Have set a not befor the tests since they are supose to be false
    assert not Fraction(1, 2) >= Fraction(3, 4)
    assert not Fraction(1, 3) == Fraction(1, 2)
    assert not Fraction(1, 3) == 2
    assert not Fraction(2 ,6) > Fraction(2, 3)
    assert not Fraction(4, 8) >= 2
    assert not Fraction(4, 8) > 2
    assert not Fraction(4, 8) < Fraction(1, 2)
    #Chec if the boolean terms gives the right errors for diffrent values
    assert (Fraction(4, 8) < 1.2) == NotImplementedError
    assert (Fraction(1, 2) == 1.2) == NotImplementedError
    assert (Fraction(1, 2) != 1.2) == NotImplementedError
    assert (Fraction(1, 2) <= 1.2) == NotImplementedError
    assert (Fraction(1, 2) > 1.2) == NotImplementedError
    assert (Fraction(1, 2) >= 1.2) == NotImplementedError